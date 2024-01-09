from typing import Union

import numpy as np
import whisper


# TODO: this would probably be better with dependency injection
#  i.e passing an instance of the model to the class instead
class WhisperTranscriber:
    def __init__(self, model: str):
        self.model = WhisperTranscriber.get_model(model)

    @staticmethod
    def list_models() -> list[str]:
        return whisper.available_models()

    @staticmethod
    def get_model(model_name: str) -> whisper.Whisper:
        return whisper.load_model(model_name)

    def transcribe(self, audio: Union[str, np.ndarray]) -> str:
        return self.model.transcribe(audio=audio)
