from dataclasses import dataclass


@dataclass
class Transcription:
    text: str
    transcription_model: str
    hotwords: list
