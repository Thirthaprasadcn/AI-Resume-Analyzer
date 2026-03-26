import streamlit as st
import pdfplumber

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# 🌈 FULL ANIMATED CSS
st.markdown("""
<style>

/* Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    font-family: 'Poppins', sans-serif;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Title Animation */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: white;
    text-shadow: 0 0 10px #fff, 0 0 20px #ff6ec4;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #fff, 0 0 20px #ff6ec4; }
    to { text-shadow: 0 0 20px #fff, 0 0 40px #7873f5; }
}

/* Glass Cards */
.card {
    background: rgba(255,255,255,0.2);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Skill Tags */
.skill {
    display: inline-block;
    padding: 6px 14px;
    margin: 5px;
    border-radius: 20px;
    background: linear-gradient(45deg, #ff6ec4, #7873f5);
    color: white;
    font-size: 14px;
    animation: pop 0.5s ease;
}

@keyframes pop {
    from { transform: scale(0.5); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

/* Neon Buttons */
.stButton>button {
    background: linear-gradient(45deg, #ff6ec4, #7873f5);
    color: white;
    border-radius: 30px;
    padding: 12px 25px;
    font-size: 16px;
    border: none;
    box-shadow: 0 0 10px #ff6ec4;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.1);
    box-shadow: 0 0 20px #7873f5, 0 0 40px #ff6ec4;
}

/* Progress Bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #ff6ec4, #7873f5);
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🚀 AI Resume Analyzer</div>', unsafe_allow_html=True)
st.write("### Analyze your resume with style ✨")

# Upload + button
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
analyze_btn = st.button("✨ Analyze Resume")

job_desc = st.text_area("💼 Paste Job Description (Optional)")

if uploaded_file and analyze_btn:
    try:
        text = ""

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        if text.strip() == "":
            st.error("⚠️ Could not extract text")
        else:
            col1, col2 = st.columns(2)

            # Preview
            with col1:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("📄 Resume Preview")
                st.write(text[:600])
                st.markdown('</div>', unsafe_allow_html=True)

            # Skills
            with col2:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("🧠 Skills")

                SKILLS = ["python","machine learning","data science","sql","java","c++"]

                found = [s for s in SKILLS if s in text.lower()]

                if found:
                    for skill in found:
                        st.markdown(f'<span class="skill">{skill}</span>', unsafe_allow_html=True)
                else:
                    st.write("No skills found")

                st.markdown('</div>', unsafe_allow_html=True)

            # Score
            score = 0
            if len(text) > 300:
                score += 40
            if "project" in text.lower():
                score += 30
            if "experience" in text.lower():
                score += 30

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📊 Resume Score")
            st.progress(score)
            st.write(f"### {score}/100")
            st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("👆 Upload resume and click Analyze")