def run_text_to_audio():
    import streamlit as st
    from googletrans import Translator, LANGUAGES
    from gtts import gTTS
    import tempfile
    import os
    from docx import Document
    import fitz  # PyMuPDF

    # Supported languages for gTTS speech synthesis
    speech_langs = {
        "af": "Afrikaans", "ar": "Arabic", "bg": "Bulgarian", "bn": "Bengali",
        "ca": "Catalan", "cs": "Czech", "cy": "Welsh", "da": "Danish", "de": "German",
        "el": "Greek", "en": "English", "eo": "Esperanto", "es": "Spanish", "et": "Estonian",
        "fi": "Finnish", "fr": "French", "gu": "Gujarati", "hi": "Hindi", "hr": "Croatian",
        "hu": "Hungarian", "id": "Indonesian", "is": "Icelandic", "it": "Italian",
        "ja": "Japanese", "jw": "Javanese", "km": "Khmer", "kn": "Kannada", "ko": "Korean",
        "la": "Latin", "lv": "Latvian", "ml": "Malayalam", "mr": "Marathi", "my": "Myanmar (Burmese)",
        "ne": "Nepali", "nl": "Dutch", "no": "Norwegian", "pl": "Polish", "pt": "Portuguese",
        "ro": "Romanian", "ru": "Russian", "si": "Sinhala", "sk": "Slovak", "sq": "Albanian",
        "sr": "Serbian", "su": "Sundanese", "sv": "Swedish", "sw": "Swahili", "ta": "Tamil",
        "te": "Telugu", "th": "Thai", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu",
        "vi": "Vietnamese", "zh-CN": "Chinese"
    }

    # Session states
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""
    if "translated_text" not in st.session_state:
        st.session_state.translated_text = ""
    if "audio_files" not in st.session_state:
        st.session_state.audio_files = {}
    if "audio_ready" not in st.session_state:
        st.session_state.audio_ready = False

    # --- INPUT SECTION ---
    st.markdown("### Input Method")
    input_method = st.radio("Choose how to provide input:", ("Paste Text", "Upload File"))

    if input_method == "Paste Text":
        text_input = st.text_area("Enter text (or paste)", height=200)
        if st.button("Use This Text"):
            st.session_state.input_text = text_input
            st.session_state.translated_text = text_input
            st.session_state.audio_ready = False

    elif input_method == "Upload File":
        file = st.file_uploader("Upload a .txt, .docx or .pdf file", type=["txt", "docx", "pdf"])
        if file and st.button("Use File Content"):
            try:
                if file.name.endswith(".txt"):
                    st.session_state.input_text = file.read().decode("utf-8")
                elif file.name.endswith(".docx"):
                    doc = Document(file)
                    st.session_state.input_text = "\n".join([p.text for p in doc.paragraphs])
                elif file.name.endswith(".pdf"):
                    pdf = fitz.open(stream=file.read(), filetype="pdf")
                    text = ""
                    for page in pdf:
                        text += page.get_text()
                    st.session_state.input_text = text
                st.session_state.translated_text = st.session_state.input_text
                st.session_state.audio_ready = False
            except Exception as e:
                st.error(f"Error reading file: {e}")

    # --- DISPLAY + TRANSLATION ---
    if st.session_state.input_text:
        st.subheader("Original Text")
        st.markdown(st.session_state.input_text)

        st.markdown("---")
        st.subheader("Translation Options")

        translator = Translator()

        lang_options = {"Keep Original": "original"}
        for code, name in LANGUAGES.items():
            lang_options[name.title()] = code
        lang_options = dict(sorted(lang_options.items(), key=lambda item: item[0]))

        target_lang = st.selectbox("Translate to", options=list(lang_options.keys()))

        if target_lang != "Keep Original":
            target_code = lang_options[target_lang]
            translated = translator.translate(st.session_state.input_text, dest=target_code)
            st.session_state.translated_text = translated.text
        else:
            st.session_state.translated_text = st.session_state.input_text

        st.subheader("Translated Text")
        st.markdown(st.session_state.translated_text)

        st.markdown("---")
        st.subheader("Audio Generation Options")

        text_selection = st.selectbox(
            "Select which text to convert to audio:",
            ["Original Text", "Translated Text"]
        )

        selected_text = st.session_state.input_text if text_selection == "Original Text" else st.session_state.translated_text
        selected_lang_code = "en" if text_selection == "Original Text" else lang_options.get(target_lang, "en")

        if st.button("Generate Audio"):
            st.session_state.audio_files = {}

            if selected_lang_code in speech_langs:
                try:
                    tts = gTTS(text=selected_text, lang=selected_lang_code)
                    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                    tts.save(tmp.name)
                    st.session_state.audio_files[text_selection] = tmp.name
                    st.session_state.audio_ready = True
                    st.success(f"Audio for {text_selection} generated successfully!")
                except Exception as e:
                    st.error(f"Error generating audio: {e}")
            else:
                st.warning(f"Text-to-Speech not supported for language: {target_lang}")

        if st.session_state.audio_ready:
            for label, path in st.session_state.audio_files.items():
                st.audio(path)
                with open(path, "rb") as file:
                    st.download_button(
                        label=f"📥 Download {label} (MP3)",
                        data=file,
                        file_name=f"{label.replace(' ', '_').lower()}.mp3",
                        mime="audio/mpeg"
                    )