import os
import streamlit as st

from src.whisper_transcriber import WhisperTranscriber
from src.chat_summarizer import ChatSummarizer
from src.youtube import download_audio

YOUTUBE_DIR = "youtube"


@st.cache_resource
def load_whisper(model_name: str) -> WhisperTranscriber:
    return WhisperTranscriber(model_name)


@st.cache_resource
def load_gpt(model_name: str, openai_key: str) -> ChatSummarizer:
    return ChatSummarizer(openai_key, model_name)


def is_youtube_link(link: str) -> bool:
    return link.startswith("https://www.youtube.com/watch?v=")


st.title("Summarizer")

summary = None

with st.sidebar:
    whisper_options = WhisperTranscriber.list_models()
    gpt_options = ChatSummarizer.list_models()
    whisper_model = st.selectbox("TTS Model", whisper_options, index=0)
    gpt_model = st.selectbox("Summarizer Model", gpt_options, index=8)
    openai_api_key = st.text_input("OpenAI API Key")

    audio_input_path = st.text_input(
        "Or enter a path to an audio file or youtube video"
    )

    if audio_input_path:
        if is_youtube_link(audio_input_path):
            output_path = os.path.join(YOUTUBE_DIR, audio_input_path.split("=")[-1])
            audio_input_path = download_audio(audio_input_path, output_path)

        transcriber = load_whisper(whisper_model)
        transcription = transcriber.transcribe(audio_input_path)["text"]

        summarizer = load_gpt(gpt_model, openai_api_key)
        summary = summarizer.summarize(transcription)

st.title("Summary")
if summary:
    st.write(summary)
