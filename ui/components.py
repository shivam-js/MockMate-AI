import streamlit as st

def sidebar():

    with st.sidebar:

        st.title("MockMate AI")

        st.markdown("---")

        st.subheader("Developer")
        st.write("Shivam Prasad")

        st.markdown("---")

        st.subheader("Platform Features")

        st.write("Resume Based Questions")
        st.write("Voice Answer Recording")
        st.write("AI Follow-Up Questions")
        st.write("Interview Evaluation")

        st.markdown("---")

        st.caption("Version 1.0")