import streamlit as st
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from audio_recorder_streamlit import audio_recorder

from core.resume_parser import extract_resume_text
from core.skill_extractor import extract_skills
from core.question_engine import generate_questions
from core.followup_engine import generate_followup
from core.voice_engine import transcribe_audio
from core.evaluator import evaluate_full_interview
from ui.components import sidebar


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(page_title="MockMate-AI", layout="wide")

sidebar()


# --------------------------------------------------
# UI STYLE
# --------------------------------------------------

st.markdown(
"""
<style>

.main-title{
font-size:42px;
font-weight:800;
background: linear-gradient(90deg,#4A90E2,#50E3C2);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}

.question-card{
padding:20px;
border-radius:12px;
background:#1e1e1e;
border:1px solid #333;
color:white;
font-size:18px;
animation: slideFade 0.6s ease-in-out;
}

.recorder-card{
padding:20px;
border-radius:12px;
border:1px solid #333;
background:#111;
}

@keyframes slideFade{
0%{opacity:0; transform:translateY(20px);}
100%{opacity:1; transform:translateY(0px);}
}

</style>
""",
unsafe_allow_html=True
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown('<div class="main-title">MockMate-AI</div>', unsafe_allow_html=True)
st.caption("AI Powered Mock Interview System")


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

def init_state():

    defaults = {

        "questions": [],
        "q_index": 0,

        "followup_mode": False,
        "followup_question": None,

        "rec_key_main": 0,
        "rec_key_follow": 0,

        "followup_count": 0,
        "max_followups": 2,

        "play_animation": False,

        "answers": [],

        "interview_count": 0,
        "max_interviews": 3
    }

    for k in defaults:
        if k not in st.session_state:
            st.session_state[k] = defaults[k]

init_state()


# --------------------------------------------------
# RESUME UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


if uploaded_file:

    # ----------------------------------------------
    # INTERVIEW LIMIT
    # ----------------------------------------------

    if st.session_state.interview_count >= st.session_state.max_interviews:

        st.error("You have reached the maximum interview limit.")

        st.stop()


    # ----------------------------------------------
    # RESUME PROCESSING
    # ----------------------------------------------

    resume_text = extract_resume_text(uploaded_file)

    skills = extract_skills(resume_text)

    st.success(f"Detected Skills: {skills}")


    # ----------------------------------------------
    # GENERATE QUESTIONS
    # ----------------------------------------------

    if not st.session_state.questions:

        st.session_state.questions = generate_questions(skills)


    total_q = len(st.session_state.questions)
    current_q = st.session_state.q_index + 1


    # ----------------------------------------------
    # PROGRESS BAR
    # ----------------------------------------------

    progress = st.session_state.q_index / total_q

    st.markdown(f"### Question {current_q} / {total_q}")

    st.progress(progress)


    # ----------------------------------------------
    # TRANSITION ANIMATION
    # ----------------------------------------------

    if st.session_state.play_animation:

        st.success("Previous question completed. Moving to next question.")

        st.balloons()

        components.html(
        """
        <script>
        window.parent.document.querySelector('section.main').scrollTo({
        top:0,
        behavior:'smooth'
        });
        </script>
        """,
        height=0
        )

        st.session_state.play_animation = False


    # --------------------------------------------------
    # MAIN INTERVIEW FLOW
    # --------------------------------------------------

    if st.session_state.q_index < len(st.session_state.questions):

        question = st.session_state.questions[st.session_state.q_index]

        st.subheader("Interview Question")

        st.markdown(
        f'<div class="question-card">{question}</div>',
        unsafe_allow_html=True
        )


        # --------------------------------------------------
        # MAIN QUESTION RECORDING
        # --------------------------------------------------

        if not st.session_state.followup_mode:

            st.subheader("Record Your Answer")

            st.markdown('<div class="recorder-card">', unsafe_allow_html=True)

            audio_main = audio_recorder(
                text="Record / Pause",
                icon_name="microphone",
                recording_color="#ff4b4b",
                neutral_color="#2ecc71",
                key=f"main_rec_{st.session_state.rec_key_main}"
            )

            st.markdown('</div>', unsafe_allow_html=True)


            if audio_main:

                st.audio(audio_main)

                if st.button("Submit Answer"):

                    text = transcribe_audio(audio_main)

                    st.session_state.answers.append(text)

                    # AI FOLLOWUP
                    st.session_state.followup_question = generate_followup(text, skills)

                    st.session_state.followup_mode = True

                    st.session_state.followup_count = 1

                    st.session_state.rec_key_main += 1

                    st.rerun()


        # --------------------------------------------------
        # FOLLOW-UP MODE
        # --------------------------------------------------

        else:

            st.subheader("Follow-Up Question")

            st.markdown(
            f'<div class="question-card">{st.session_state.followup_question}</div>',
            unsafe_allow_html=True
            )

            st.subheader("Record Follow-Up Answer")

            st.markdown('<div class="recorder-card">', unsafe_allow_html=True)

            audio_follow = audio_recorder(
                text="Record / Pause",
                icon_name="microphone",
                recording_color="#ff4b4b",
                neutral_color="#2ecc71",
                key=f"follow_rec_{st.session_state.rec_key_follow}"
            )

            st.markdown('</div>', unsafe_allow_html=True)


            if audio_follow:

                st.audio(audio_follow)

                if st.button("Submit Follow-Up"):

                    text = transcribe_audio(audio_follow)

                    st.session_state.answers.append(text)


                    # FOLLOW-UP CHAIN
                    if st.session_state.followup_count < st.session_state.max_followups:

                        st.session_state.followup_question = generate_followup(text, skills)

                        st.session_state.followup_count += 1


                    else:

                        st.session_state.followup_mode = False

                        st.session_state.followup_question = None

                        st.session_state.followup_count = 0

                        st.session_state.q_index += 1

                        st.session_state.play_animation = True


                    st.session_state.rec_key_follow += 1

                    st.rerun()


    # --------------------------------------------------
    # INTERVIEW COMPLETE
    # --------------------------------------------------

    else:

        st.subheader("Interview Completed")

        metrics, feedback = evaluate_full_interview(
            resume_text,
            st.session_state.answers
        )

        st.write("### Final Interview Score:", metrics["overall"])


        # ----------------------------------------------
        # PERFORMANCE DASHBOARD
        # ----------------------------------------------

        st.markdown("### Performance Dashboard")

        st.progress(metrics["technical"]/100)
        st.write("Technical Knowledge:", metrics["technical"])

        st.progress(metrics["communication"]/100)
        st.write("Communication:", metrics["communication"])

        st.progress(metrics["confidence"]/100)
        st.write("Confidence:", metrics["confidence"])

        st.progress(metrics["structure"]/100)
        st.write("Answer Structure:", metrics["structure"])


        # ----------------------------------------------
        # SCORE PIE CHART
        # ----------------------------------------------

        fig, ax = plt.subplots()

        ax.pie(
        [metrics["overall"], 100 - metrics["overall"]],
        labels=["Score","Improvement"],
        autopct="%1.0f%%"
        )

        st.pyplot(fig)


        # ----------------------------------------------
        # FEEDBACK
        # ----------------------------------------------

        for f in feedback:
            st.write("•", f)


        st.session_state.interview_count += 1
