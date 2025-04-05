import streamlit as st
import requests

st.set_page_config(page_title="SentiSolve Nexus", layout="wide")
st.title("🧠 SentiSolve Nexus – GenAI for Support Automation")

ticket_text = st.text_area("Paste your support ticket here:")

if st.button("Analyze Ticket"):
    with st.spinner("Analyzing with SentiSolve agents..."):
        res = requests.post("http://localhost:8000/analyze", json={"ticket_text": ticket_text})
        data = res.json()

        st.subheader("🔎 Summary")
        st.write(data['summary'])

        st.subheader("🧠 Predicted Root Cause")
        st.success(data['root_cause'])

        st.subheader("📄 Suggested Resolution")
        st.info(data['recommended_resolution'])
        st.write(f"Similarity Score: {data['similarity_score']}%")

        st.subheader("🧭 Routed Team")
        st.warning(data['routed_team'])

        st.subheader("⏱️ Estimated Resolution Time")
        st.code(f"{data['eta_hours']} hours")
