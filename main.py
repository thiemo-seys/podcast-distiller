import argparse
import os

from src.whisper_transcriber import WhisperTranscriber
from src.chat_summarizer import ChatSummarizer


def main():
    args = parser.parse_args()

    transcriber = WhisperTranscriber(args.wisper_model)
    print("loaded whisper model")
    transcription = transcriber.transcribe(args.input)["text"]
    print(f"{transcription=}")

    summarizer = ChatSummarizer(args.openai_api_key, args.chat_model)
    summary = summarizer.summarize(transcription)
    print(f"{summary=}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converts mp3 to text and summarizes the text.")
    parser.add_argument("-i", "--input", help="The file to summarize", type=str, required=True)
    parser.add_argument("-o", "--output", help="The file to save the summarized notes to", type=str)
    parser.add_argument("-oa", "--openai_api_key", help="OpenAI api key", type=str,
                        default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("-cm", "--chat_model", help="ChatGPT model name", type=str,
                        default=os.environ.get("CHAT_MODEL"))
    parser.add_argument("-wm", "--wisper_model", help="Whisper model name", type=str,
                        default=os.environ.get("WHISPER_MODEL"))
    main()
