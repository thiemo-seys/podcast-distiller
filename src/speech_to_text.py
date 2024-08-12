from typing import Union

import numpy as np
import whisper


def list_models() -> list[str]:
    """List all available models"""
    return whisper.available_models()


def get_model(model_name: str) -> whisper.Whisper:
    """Load the whisper given model"""
    return whisper.load_model(model_name)


def transcribe(model: whisper.Whisper, audio: Union[str, np.ndarray]) -> str:
    return model.transcribe(audio=audio)


class Transcriber:
    def __init__(self, model: whisper.Whisper = None):
        self.model = model

    def transcribe(self, audio: Union[str, np.ndarray]) -> str:
        return transcribe(self.model, audio)
