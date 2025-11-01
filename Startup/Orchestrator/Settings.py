from dataclasses import dataclass
from typing import Dict
import json
import os


@dataclass
class N8N(object):
    name: str
    container_name: str
    ports: Dict[str, str]
    environment: Dict[str, str]
    volumes: Dict[str, str]
    network: str
    version: str


@dataclass
class N8NSettings(object):
    N8N: N8N

    @classmethod
    def load(cls) -> "N8NSettings":
        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, "orchestrator-settings.json")
        with open(json_path, "r") as f:
            config = json.load(f)

        n8n_settings = N8N(**config.get("n8n", {}))

        return cls(n8n_settings)
