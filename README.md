# MockMate-AI 🤖

AI-powered mock interview system that analyzes resumes, generates interview questions, records answers, and evaluates candidate performance.

## 🔗 Live Demo

https://mockmate-ai-3xjowtbsbxtqerxuqilw8w.streamlit.app/

---

## Screenshots

### Home Page
![Home](assets/Home.png)

### Resume Upload
![Resume Upload](assets/ResumeUpload.png)

### Interview Page
![Interview](assets/Interview.png)

### Evaluation Page
![Evaluation](assets/Evaluation.png)

### Result Page
![Result](assets/Result.png)

## 🚀 Features

• Resume Parsing from PDF
• Automatic Skill Extraction using NLP
• AI Generated Interview Questions
• Dynamic Follow-Up Questions
• Voice Answer Recording
• Interview Evaluation System

---

## 🛠 Tech Stack

Frontend
• Streamlit

Backend
• Python

AI / NLP
• TF-IDF
• Cosine Similarity
• NLP Skill Extraction

Libraries
• Streamlit
• Scikit-learn
• PyPDF2
• Matplotlib

---

## 📂 Project Structure

MockMate-AI
│
├── core/                    # AI logic and backend processing
│   ├── evaluator.py
│   ├── followup_engine.py
│   ├── question_engine.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── voice_engine.py
│
├── ui/                      # UI components and layout
│   └── components.py
│
├── assets/                  # Images used in README
│   ├── Home.png
│   ├── ResumeUpload.png
│   ├── Interview.png
│   ├── Evaluation.png
│   └── Result.png
│
├── README.md                # Project documentation
├── .gitignore               # Files ignored by git
├── requirements.txt         # Python dependencies
└── app.py                   # Main Streamlit application

---

## ⚙️ How to Run Locally

Clone the repository

git clone https://github.com/shivam-js/MockMate-AI.git

Navigate to the project folder

cd MockMate-AI

Install required dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

streamlit run app.py

---

## 👨‍💻 Author

Shivam Prasad

