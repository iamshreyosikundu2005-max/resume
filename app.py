import streamlit as st
import PyPDF2
import docx
import re

# Title
st.title("📄 AI Resume Analyzer")

# Skill Database
skills_db = [
    "python", "java", "c++", "machine learning", "sql",
    "html", "css", "javascript", "data analysis",
    "communication", "leadership", "excel"
]

# Job Recommendation Rules
job_roles = {
    "python": "Python Developer",
    "machine learning": "ML Engineer",
    "sql": "Database Developer",
    "html": "Web Developer",
    "javascript": "Frontend Developer",
    "excel": "Data Analyst"
}

# Extract text from PDF
def read_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Extract text from DOCX
def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

# File Upload
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:

    file_type = uploaded_file.name.split(".")[-1]

    if file_type == "pdf":
        resume_text = read_pdf(uploaded_file)

    elif file_type == "docx":
        resume_text = read_docx(uploaded_file)

    st.subheader("📌 Resume Content")
    st.write(resume_text[:1000])

    # Lowercase text
    text = resume_text.lower()

    # Skill Detection
    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    st.subheader("✅ Detected Skills")
    st.write(found_skills)

    # Resume Score
    score = len(found_skills) * 10
    if score > 100:
        score = 100

    st.subheader("📊 Resume Score")
    st.progress(score)
    st.write(score, "/100")

    # Job Recommendation
    st.subheader("💼 Recommended Jobs")

    jobs = set()

    for skill in found_skills:
        if skill in job_roles:
            jobs.add(job_roles[skill])

    st.write(list(jobs))

    # Suggestions
    st.subheader("🤖 Suggestions")

    if score < 50:
        st.write("Add more technical skills.")
        st.write("Improve formatting.")
        st.write("Add projects section.")
    else:
        st.write("Good Resume! Add certifications for better chances.")
        import streamlit as st

st.title("📄 AI Resume Analyzer")
st.write("Project is running successfully!")