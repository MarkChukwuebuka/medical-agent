import streamlit as st
from orchestrator import InfectAI
import json

st.set_page_config(page_title="InfectAI", page_icon="🦠")

st.title("🦠 InfectAI")
st.markdown("Intelligent Infectious Disease Risk Assessment System")

symptoms = st.text_area("Enter patient symptoms:")

if st.button("Assess Risk"):

    if symptoms.strip() == "":
        st.warning("Please enter symptoms.")
    else:
        with st.spinner("Analyzing symptoms..."):
            result = InfectAI.assess(symptoms)

        try:
            data = json.loads(result)

            st.subheader("Assessment Result")

            st.metric("Risk Level", data["Risk_Level"])
            st.write("**Infection Probability:**", data["Infection_Probability"])
            st.write("**Suspected Infection:**", data["Suspected_Infection"])
            st.write("**Explanation:**", data["Explanation"])
            st.write("**Recommended Action:**", data["Recommended_Action"])

        except:
            st.error("Model returned invalid format. Check logs.")