from dataclasses import dataclass
from typing import Dict
import json
import os


@dataclass
class PostgresSettings(object):
    host: str
    ports: Dict[str, int]
    environment: Dict[str, str]
    volumes: Dict[str, str]
    name: str
    network: str
    version: int


@dataclass
class RedisSettings(object):
    host: str
    ports: int
    database_name: int
    volumes: Dict[str, str]
    name: str
    network: str
    version: int


@dataclass
class MongoDBSettings(object):
    host: str
    ports: int
    database_name: str
    volumes: Dict[str, str]
    name: str
    network: str
    version: int


@dataclass
class ElasticSearchSettings(object):
    host: str
    ports: int
    version: str
    name: str
    environment: Dict[str, str]
    volumes: Dict[str, str]
    network: str
    scheme: str


@dataclass
class DatabaseSettings(object):
    postgres_settings: PostgresSettings
    redis_settings: RedisSettings
    mongo_settings: MongoDBSettings
    elasticsearch_settings: ElasticSearchSettings

    @classmethod
    def load(cls) -> "DatabaseSettings":
        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, "database-settings.json")
        with open(json_path, "r") as f:
            config = json.load(f)

        postgres_settings = PostgresSettings(**config.get("postgres", {}))
        redis_settings = RedisSettings(**config.get("redis", {}))
        mongo_settings = MongoDBSettings(**config.get("mongodb", {}))
        elasticsearch_settings = ElasticSearchSettings(**config.get("elasticsearch", {}))

        return cls(postgres_settings, redis_settings, mongo_settings, elasticsearch_settings)

