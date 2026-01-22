
import streamlit as st
st.title("AI Career Skill-Gap Analyzer")
st.write("Let's see what you need to reach your goal")
st.divider()
#selecting role
role=st.selectbox("Choose Your Target Role",["Software Developer","Data Analyst","Cybersecurity Engineer","Full Stack Developer","Backend Developer","Frontend Developer"])

#resume input
resume_text=st.text_area("Please paste your resume",height=200,placeholder="Paste here...")

#temporary action button
if(st.button("Analyze Skill Gap")):
    st.success(f"Analyzing resume for the role:{role}")
    st.info("SKill Gap Analysis logic coming next!")