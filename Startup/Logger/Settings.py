from dataclasses import dataclass
from typing import Dict
import json
import os


@dataclass
class GrayLog(object):
    name: str
    container_name: str
    ports: Dict[str, str]
    environment: Dict[str, str]
    volumes: Dict[str, str]
    network: str
    version: str


@dataclass
class LoggerSettings(object):
    GrayLog: GrayLog

    @classmethod
    def load(cls) -> "LoggerSettings":
        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, "logger-settings.json")
        with open(json_path, "r") as f:
            config = json.load(f)

        graylog_settings = GrayLog(**config.get("graylog", {}))

        return cls(graylog_settings)
