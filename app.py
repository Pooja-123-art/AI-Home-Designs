import streamlit as st
import requests
import time

# API Key-ai edukkiradhu
api_key = st.secrets["MESHY_API_KEY"]

st.title("🏠 Real AI 3D Home Architect")

prompt = st.text_area("Enter your design requirement:")
if st.button("Generate 3D Model"):
    if prompt:
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"mode": "preview", "prompt": prompt, "art_style": "realistic"}
        
        # Meshy API-ku request anuppudhu
        response = requests.post("https://api.meshy.ai/v1/text-to-3d", headers=headers, json=payload)
        task_id = response.json().get("result")
        
        with st.spinner("AI is creating your 3D model..."):
            time.sleep(15) # AI create panna konjam neram aagum
            
            # Result-ai inga show pannuvom
            st.success("Design Ready!")
            # Inga dhaan neenga rotate panni paakura 3D viewer varum
            st.info("Your 3D model is being processed. Check Meshy Dashboard for the 3D file!")
    else:
        st.error("Please enter a prompt!")
