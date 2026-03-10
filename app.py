import streamlit as st
import requests
import time

# --- Page Layout (Figma Design-ku yetha maari) ---
st.set_page_config(page_title="AI 3D Architect", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #6200EE; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 AI 3D Home Architect")
st.write("Convert your ideas into 3D designs instantly.")

# --- Requirement Input Section ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Your Requirements")
    user_prompt = st.text_area("Type here (Example: Modern living room with wooden floor)", height=200)
    generate_btn = st.button("Generate 3D Model")

with col2:
    st.subheader("3D Preview Result")
    if generate_btn:
        if user_prompt:
            with st.spinner("AI is building your 3D model..."):
                # --- Meshy AI Integration Logic ---
                # API_KEY = "YOUR_MESHY_API_KEY"
                # headers = {"Authorization": f"Bearer {API_KEY}"}
                # payload = {"mode": "preview", "prompt": user_prompt}
                # response = requests.post("https://api.meshy.ai/v1/text-to-3d", headers=headers, json=payload)

                time.sleep(4) # AI processing simulation

                st.success("3D Design Generated!")
                # Inga real 3D model viewer load aagum
                st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Placeholder for 3D animation
                st.download_button("Download 3D File (.glb)", "file_data", file_name="home_design.glb")
        else:
            st.warning("Please enter your requirement first!")