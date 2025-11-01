from dataclasses import dataclass
from typing import Dict
import json
import os


@dataclass
class SDKSettings(object):
    name: str
    container_name: str
    ports: Dict[str, str]
    environment: Dict[str, str]
    volumes: Dict[str, str]
    network: str
    version: str


@dataclass
class DatabaseSettings(object):
    SDK_settings: SDKSettings

    @classmethod
    def load(cls) -> "DatabaseSettings":
        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, "sdk-settings.json")
        with open(json_path, "r") as f:
            config = json.load(f)

        sdk_settings = SDKSettings(**config.get("python", {}))

        return cls(sdk_settings)
