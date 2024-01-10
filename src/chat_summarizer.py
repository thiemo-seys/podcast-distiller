from openai import OpenAI

DEFAULT_SUMMARY_CONTEXT = """
    You are a helpful secretary that needs to summarize a meeting transcription.
    Provide a concise summary of the text transcription from the video, highlight key points and main ideas."
"""


class ChatSummarizer:
    def __init__(
        self,
        api_key: str,
        model: str,
        temperature: float = 0.5,
        context: str = DEFAULT_SUMMARY_CONTEXT,
    ):
        self.client = OpenAI(api_key=api_key)
        self.context = context
        self.temperature = temperature
        self.model = model

    @staticmethod
    def list_models() -> list[str]:
        return [
            "gpt-4-1106-preview",
            "gpt-4-vision-preview",
            "gpt-4",
            "gpt-4-0314",
            "gpt-4-0613",
            "gpt-4-32k",
            "gpt-4-32k-0314",
            "gpt-4-32k-0613",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-0301",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-16k-0613",
        ]

    def summarize(self, prompt: str):
        messages = self._generate_messages(prompt)

        response = self.client.chat.completions.create(
            model=self.model, messages=messages, temperature=self.temperature
        )
        return response.choices[0].message.content

    def _generate_messages(self, prompt: str):
        return [
            {"role": "user", "content": prompt},
            {"role": "system", "content": self.context},
        ]
