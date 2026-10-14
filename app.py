import os
import streamlit as st
from google import genai

# Page Config
st.set_page_config(
    page_title="AI Script Generator", page_icon="🎬", layout="centered"
)

st.title("🎬 AI Social Media Script Generator")
st.write(
    "Generate viral scripts for Instagram Reels, YouTube Shorts, and Videos instantly!"
)

# Sidebar - Gumroad Passcode & Gemini API Key
st.sidebar.header("🔑 Authentication")
passcode = st.sidebar.text_input("Enter Gumroad Passcode:", type="password")

# Secret Passcode
SECRET_PASSCODE = "SCRIPTPRO2026"

if passcode != SECRET_PASSCODE:
    st.warning("🔒 Please enter a valid Gumroad Access Passcode to use this tool.")
    st.info("Purchase the passcode to get access.")
else:
    api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

    topic = st.text_input("Enter Video Topic / Subject:")
    platform = st.selectbox(
        "Select Platform:", ["Instagram Reel", "YouTube Shorts", "YouTube Video"]
    )
    
    # Added Tamil, Telugu, and Hindi to the language options list
    language = st.selectbox(
        "Select Language:", 
        ["English", "Malayalam", "Hindi", "Tamil", "Telugu"]
    )

    if st.button("Generate Script 🚀"):
        if not api_key:
            st.error("Please provide a Gemini API Key!")
        elif not topic:
            st.error("Please enter a video topic!")
        else:
            try:
                client = genai.Client(api_key=api_key)
                
                prompt = (
                    f"Create a viral {platform} script in {language} about: {topic}. "
                    f"Include a strong hook, body content, and a clear call to action (CTA). "
                    f"Do not use blockquotes ('>') or italicized gray text. "
                    f"Write all text in standard bold or regular bold plain text format for maximum readability."
                )

                with st.spinner("Generating script..."):
                    response = client.models.generate_content(
                        model="gemini-3.6-flash", contents=prompt
                    )
                    st.success("Your script is ready!")
                    st.subheader("📝 Generated Script:")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")