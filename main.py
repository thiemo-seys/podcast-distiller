import argparse
import logging
import sys

from src import transcription, db_utils


def setup_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def load_transcription_repository(filename: str):
    conn = db_utils.open_connection(filename)
    return transcription.TranscriptionRepository(conn)


def main():
    logger = setup_logger()
    args = parser.parse_args()

    # check if file has already been transcribed
    transcription_repository = load_transcription_repository("database/main.sqlite")
    file_hash = db_utils.calculate_blake2(args.input)
    print(f"{file_hash=}")
    transcription_result = transcription_repository.find_by(
        file_hash=file_hash, id=1, test=2
    )
    print(f"{transcription_result=}")

    # whisper_model = get_model(args.whisper)
    # transcription = Transcriber(model=whisper_model).transcribe(args.input)
    # text = transcription["text"]
    # logger.info(f"transcription: {text}")
    #
    # summary = summarize(args.llm, text)
    # logger.info(f"summary: {summary['response']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Filepath of audio file")
    parser.add_argument(
        "-o", "--output", type=str, help="Filepath where the results will be saved to"
    )
    parser.add_argument(
        "-l",
        "--llm",
        type=str,
        default="phi3",
        help="The llm model used to summarize the transcription",
    )

    parser.add_argument(
        "-w",
        "--whisper",
        type=str,
        default="small.en",
        help="The whisper model used for transcription",
    )

    main()
