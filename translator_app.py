import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(page_title="AI Translation Tool", page_icon="🔊")
st.title("🔊 AI Translation Tool with Voice")

langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
languages = list(langs_dict.keys())

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source Language:", ["auto"] + languages)
with col2:
    dest_lang = st.selectbox("Target Language:", languages, index=languages.index("tamil"))

text_to_translate = st.text_area("Input Text:")

if st.button("Translate & Listen"):
    if text_to_translate:
        # 1. Translation logic
        translated = GoogleTranslator(source=src_lang, target=langs_dict[dest_lang]).translate(text_to_translate)
        st.success(f"Translated Text: {translated}")

        # 2. Text-to-Speech logic (Optional Task)
        try:
            tts = gTTS(text=translated, lang=langs_dict[dest_lang])
            tts.save("speech.mp3")
            st.audio("speech.mp3") # This creates a play button!
        except:
            st.info("Audio preview not available for this language.")
    else:
        st.warning("Please enter text.")