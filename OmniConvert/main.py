import streamlit as st
from audio_to_text import run_audio_to_text
from text_to_audio import run_text_to_audio

st.set_page_config(page_title="OmniConvert", layout="centered")
st.title("🧠 OmniConvert: All-in-One Media Converter")

st.markdown("""
    Welcome to **OmniConvert**, your intelligent media assistant!  
    Easily **convert between audio, text, documents, images, and video** — all in one place.
            
    Choose a mode from the sidebar to get started!""")

# Sidebar Mode Selector
mode = st.sidebar.radio(
    "Choose a Mode:",
    options=[
        "🌟 Welcome to OmniConvert!",
        "🎙️ Audio/Voice to Text",
        "🗣️ Text/Document to Audio",
        "📄 Chat with Document (Coming Soon)",
        "🖌️ Text/ to Image (Coming Soon)",
        "🖼️ Image to Text (Coming Soon)",
        "🎞️ Text to Video (Coming Soon)",
        "📹 Video to Text (Coming Soon)"
    ],
    index=None  # This prevents a default selection
)

# Feature routing
if mode == "🌟 Welcome to OmniConvert!":
    # 🌟 Landing Page Description
    st.markdown("""

    ### ✨ Current Features:
    - 🎙️ **Audio/Voice to Text**: Transcribe live or recorded audio.
    - 🗣️ **Text/Document to Audio**: Turn text or files into spoken voice.

    ### 🚧 Coming Soon:
    - 📄 **Chat with Document**
    - 🖼️ **Image to Text**
    - 📹 **Video to Text**
    - 🎞️ **Text to Video**

    """)
elif mode == "🎙️ Audio/Voice to Text":
    run_audio_to_text()
elif mode == "🗣️ Text/Document to Audio":
    run_text_to_audio()
# Future feature placeholders can be added later
