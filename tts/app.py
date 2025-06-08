
#working

import streamlit as st
from gtts import gTTS
import requests
from bs4 import BeautifulSoup
import tempfile

st.title("🗣️ Text to Speech App (with Link Reader)")

# Tabs for options
tab1, tab2 = st.tabs(["📄 Enter Text", "🌐 Extract from Link"])

# Language selection
lang_map = {"English": "en", "Hindi": "hi"}
language = st.radio("Choose Language", ["English", "Hindi"], horizontal=True)
lang_code = lang_map[language]

# Text input tab
with tab1:
    text_input = st.text_area("Enter your text here:")

# Link input tab
with tab2:
    url_input = st.text_input("Paste a webpage link to extract content:")

    if url_input:
        try:
            res = requests.get(url_input, timeout=10)
            soup = BeautifulSoup(res.text, "html.parser")
            # Extract all paragraph text
            paragraphs = soup.find_all("p")
            full_text = " ".join(p.text for p in paragraphs)
            if full_text:
                st.success("✅ Content extracted!")
                st.text_area("Extracted Text", full_text, height=200, key="extracted_text")
                text_input = full_text
            else:
                st.warning("No readable text found on this page.")
        except Exception as e:
            st.error(f"Error reading link: {e}")

# Speak button
if st.button("🔊 Convert to Speech"):
    if not text_input.strip():
        st.warning("Please enter or extract some text!")
    else:
        tts = gTTS(text=text_input, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
            st.success("✅ Speech ready and playing!")







#only text speech working
# import streamlit as st
# from gtts import gTTS
# import os
# import tempfile

# # Title
# st.title("🗣️ AI Text to Speech App (No FFmpeg!)")

# # Input box
# text = st.text_area("Enter text here:", height=200)

# # Language selection
# lang = st.selectbox("Select language", ["en", "hi", "fr", "es"])

# # Speak button
# if st.button("🔊 Speak Now"):
#     if text.strip() == "":
#         st.warning("Please enter some text first!")
#     else:
#         tts = gTTS(text=text, lang=lang)
        
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#             temp_path = fp.name
#             tts.save(temp_path)
#             st.success("✅ Speech ready!")
#             st.audio(temp_path, format="audio/mp3")


























#working

# # tts_streamlit_app.py
# import streamlit as st
# import pyttsx3
# import tempfile
# from pydub import AudioSegment
# from pydub.playback import play

# # Title
# st.title("🗣️ Text to Speech App")

# # Input text
# text = st.text_area("Enter text to convert to speech", height=200)

# # Button
# if st.button("🔊 Convert and Speak"):
#     if text.strip() == "":
#         st.warning("Please enter some text!")
#     else:
#         # Initialize TTS engine
#         engine = pyttsx3.init()
#         engine.setProperty('rate', 150)
        
#         # Save to temporary file
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
#             engine.save_to_file(text, f.name)
#             engine.runAndWait()
            
#             # Play audio using pydub
#             sound = AudioSegment.from_file(f.name, format="mp3")
#             st.audio(f.name)
#             play(sound)

