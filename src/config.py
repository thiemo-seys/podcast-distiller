import os
from dataclasses import dataclass
from pathlib import Path

import yaml

@dataclass
class PDConfig:
    openai_api_key: str = os.environ.get("OPENAI_API_KEY")
    wisper_model: str = os.environ.get("WISPER_MODEL")


def read_yaml_config(file_path: str) -> PDConfig:
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
        return PDConfig(
            **config,
        )
