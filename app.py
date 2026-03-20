import streamlit as st
from orchestrator import InfectAI
import json

# Page config
st.set_page_config(
    page_title="InfectAI",
    page_icon="🦠",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}

h1, h2, h3, h4 {
    color: #22c55e;
}

.stTextArea textarea {
    border-radius: 10px;
    border: 1px solid #22c55e;
}

.stButton button {
    background-color: #22c55e;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #111827;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 15px;
}

.metric-box {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# Header
st.title("🦠 InfectAI")
st.caption("AI-powered infectious disease risk assessment")

# Layout split
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🧾 Patient Input")
    symptoms = st.text_area(
        "Enter symptoms",
        placeholder="e.g. fever, cough, fatigue...",
        height=200
    )

    assess_btn = st.button("🚀 Assess Risk")

with col2:
    st.subheader("📊 Results")

    if assess_btn:
        if symptoms.strip() == "":
            st.warning("⚠️ Please enter symptoms.")
        else:
            with st.spinner("Analyzing symptoms..."):
                result = InfectAI.assess(symptoms)

            try:
                data = json.loads(result)

                # Risk Level (highlighted)
                st.markdown(f"""
                <div class='card'>
                    <h3>Risk Level</h3>
                    <h1>{data['Risk_Level']}</h1>
                </div>
                """, unsafe_allow_html=True)

                # Metrics row
                m1, m2 = st.columns(2)

                with m1:
                    st.markdown(f"""
                    <div class='metric-box'>
                        <h4>Infection Probability</h4>
                        <p style='font-size:20px'>{data['Infection_Probability']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                with m2:
                    st.markdown(f"""
                    <div class='metric-box'>
                        <h4>Suspected Infection</h4>
                        <p style='font-size:20px'>{data['Suspected_Infection']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                # Explanation
                st.markdown(f"""
                <div class='card'>
                    <h4>🧠 Explanation</h4>
                    <p>{data['Explanation']}</p>
                </div>
                """, unsafe_allow_html=True)

                # Recommended Action
                st.markdown(f"""
                <div class='card'>
                    <h4>💊 Recommended Action</h4>
                    <p>{data['Recommended_Action']}</p>
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error("❌ Model returned invalid format. Check logs.")
                st.text(str(e))

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | InfectAI v1.0 By Chisom")
























# import streamlit as st
# from orchestrator import InfectAI
# import json
#
# st.set_page_config(page_title="InfectAI", page_icon="🦠")
#
# st.title("🦠 InfectAI")
# st.markdown("Intelligent Infectious Disease Risk Assessment System")
#
# symptoms = st.text_area("Enter patient symptoms:")
#
# if st.button("Assess Risk"):
#
#     if symptoms.strip() == "":
#         st.warning("Please enter symptoms.")
#     else:
#         with st.spinner("Analyzing symptoms..."):
#             result = InfectAI.assess(symptoms)
#
#         try:
#             data = json.loads(result)
#
#             st.subheader("Assessment Result")
#
#             st.metric("Risk Level", data["Risk_Level"])
#             st.write("**Infection Probability:**", data["Infection_Probability"])
#             st.write("**Suspected Infection:**", data["Suspected_Infection"])
#             st.write("**Explanation:**", data["Explanation"])
#             st.write("**Recommended Action:**", data["Recommended_Action"])
#
#         except:
#             st.error("Model returned invalid format. Check logs.")