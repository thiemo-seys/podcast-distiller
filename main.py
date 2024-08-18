import argparse

from src import Transcriber, get_model, summarize


def main():
    args = parser.parse_args()

    whisper_model = get_model("tiny.en")
    transcription = Transcriber(model=whisper_model).transcribe(args.input)
    print(f"transcription: {transcription['text']}")
    summary = summarize(args.model, transcription)

    print(f"summary: {summary}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Filepath of audio file")
    parser.add_argument(
        "-o", "--output", type=str, help="Filepath where the results will be saved to"
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="llama3.1",
        help="The model to use for summarizing the transcription",
    )

    main()
