from ollama import generate

from promts import SUMMARY_PROMPT


def summarize(model, text: str):
    prompt = SUMMARY_PROMPT.substitute({"transcription": text})
    return generate(model, prompt)
