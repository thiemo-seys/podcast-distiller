from ollama import generate

from .promts import SUMMARY_PROMPT


def summarize(model: str, text: str):
    return generate(
        model,
        prompt=text,
        system=SUMMARY_PROMPT,
    )
