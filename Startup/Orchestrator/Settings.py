from dataclasses import dataclass
from typing import Dict, Any
import json
import os


@dataclass
class N8N:
    name: str
    container_name: str
    ports: Dict[str, Any]
    environment: Dict[str, Any]
    volumes: Dict[str, Any]
    network: str
    version: str


@dataclass
class Langflow:
    name: str
    container_name: str
    ports: Dict[str, Any]
    environment: Dict[str, Any]
    volumes: Dict[str, Any]
    network: str
    version: str


@dataclass
class OrchestratorSettings:
    n8n: N8N | None = None
    langflow: Langflow | None = None

    @classmethod
    def load(cls) -> "OrchestratorSettings":
        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, "orchestrator-settings.json")

        with open(json_path, "r") as f:
            config = json.load(f)

        n8n_cfg = config.get("n8n")
        langflow_cfg = config.get("langflow")

        n8n = N8N(**n8n_cfg) if n8n_cfg else None
        langflow = Langflow(**langflow_cfg) if langflow_cfg else None

        return cls(n8n=n8n, langflow=langflow)
