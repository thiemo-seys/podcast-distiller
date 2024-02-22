from typing import Union

import numpy as np
import whisper


class WhisperTranscriber:
    def __init__(self, model: str):
        self.model = WhisperTranscriber.get_model(model)

    @staticmethod
    def list_models() -> list[str]:
        """List all available models"""
        return whisper.available_models()

    @staticmethod
    def get_model(model_name: str) -> whisper.Whisper:
        """Load the whisper model"""
        return whisper.load_model(model_name)

    def transcribe(self, audio: Union[str, np.ndarray]) -> str:
        """Transcribe the audio"""
        return self.model.transcribe(audio=audio)
