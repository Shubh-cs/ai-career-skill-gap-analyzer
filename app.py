
import streamlit as st
#skill set
Role_Skill={"Software Developer(Backend)":["python","django","node","sql","git","rest api","authentication"],
            "Quant Developer":["c++","python","data structures","algorithms","probabilty","statics","numpy"],
            "Data Analyst":["excel","power bi","sql","pandas","tableau","python","data visualization"],
            "Cybersecurity Engineer":["networking","linux","owasp","nmap","burp suite","cryptography","vulnerability assesment"],
            "Full Stack Developer":["javascript","react","node","mongodb","sql","rest api","express"],
            "DevOps Engineer":["linux","docker","ci/cd","github actions","kubernetes","aws","automation"],
            "Frontend Developer":["html","css","git","rest api","react","javascript","responsive design"],
            "Blockchain Developer":["solidity","ethereum","smart contracts","web3","hardhat","erc-20","ipfs"],
            "LLM Engineer":["python","transformers","huggingface","prompt engineering","rag","langchain","vector database"] }

#Title page
st.title("AI Career Skill-Gap Analyzer")
st.write("Let's see what you need to reach your goal")
st.divider()

#input
role=st.selectbox("Choose Your Target Role",["Software Developer(Backend)","LLM Engineer","Blockchain Developer","Quant Developer",
                                             "Data Analyst","Cybersecurity Engineer","DevOps Engineer","Full Stack Developer",
                                             "Frontend Developer"])
resume_text=st.text_area("Please paste your resume",height=200,placeholder="Paste here...")

#button+logic
if(st.button("Analyze Skill Gap")):
    resume=resume_text.lower()
    required_skill=Role_Skill[role]
    skill_found=[]
    skill_missing=[]
    for skill in required_skill:
        if skill in resume:
            skill_found.append(skill)
        else:
            skill_missing.append(skill)    

    #output
    st.subheader("Results")
    st.write("Skills Found:")
    for s in skill_found:
        st.success(s)
    st.write("Skills Missing:")
    for s in skill_missing:
        st.error(s)


    ##roadmap 
    st.subheader("📌 Next Steps")

    if skill_missing:
        st.write("In the next 30 days, focus on learning:")
        for skill in skill_missing[:3]:
            st.write("➡️", skill)
    else:
        st.write("You're already matching the core skills 🎉")
