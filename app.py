
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

#roadmap generator
def generate_roadmap(missing):
    roadmap = {}

    if not missing:
        roadmap["90-Day Roadmap"] = ["You already match the core skills 🎉"]
        return roadmap

    # Split skills into 3 phases
    n = len(missing)
    phase1 = missing[: max(1, n // 3)]
    phase2 = missing[max(1, n // 3): max(2, 2 * n // 3)]
    phase3 = missing[max(2, 2 * n // 3):]

    roadmap["Days 1–30 (Foundation)"] = [
        f"Learn and practice: {', '.join(phase1)}",
        "Complete 1 small tutorial project",
        "Revise basics + make notes"
    ]

    roadmap["Days 31–60 (Application)"] = [
        f"Build projects using: {', '.join(phase2) if phase2 else 'previous skills'}",
        "Start intermediate-level problems",
        "Improve resume with new skills"
    ]

    roadmap["Days 61–90 (Job-Ready)"] = [
        f"Master advanced topics: {', '.join(phase3) if phase3 else 'remaining skills'}",
        "Build 1 strong portfolio project",
        "Start mock interviews + apply"
    ]

    return roadmap


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


    #roadmap output
    st.divider()
    st.subheader("📌 Personalized 90-Day Roadmap")

    roadmap = generate_roadmap(skill_missing)

    for phase, steps in roadmap.items():
        st.markdown(f"### {phase}")
        for step in steps:
            st.write("➡️", step)



