from Startup.Docker.Image import Image
from Startup.Docker.Container import Container
from Startup.Databases.Settings import DatabaseSettings


database_settings = DatabaseSettings.load()
image: Image = Image()
container: Container = Container()


class Databases(object):
    def __pull_postgres_if_not_exists(self):
        postgres_version: int = database_settings.postgres_settings.version
        postgres_docker_image_name: str = database_settings.postgres_settings.name
        image.pull_if_not_exists(f"{postgres_docker_image_name}:{postgres_version}")

    def __pull_redis_if_not_exists(self):
        redis_version: int = database_settings.redis_settings.version
        redis_docker_image_name: str = database_settings.redis_settings.name
        image.pull_if_not_exists(f"{redis_docker_image_name}:{redis_version}")

    def __pull_elasticsearch_if_not_exists(self):
        elasticsearch_version: str = database_settings.elasticsearch_settings.version
        elasticsearch_docker_image_name: str = database_settings.elasticsearch_settings.name
        image.pull_if_not_exists(f"{elasticsearch_docker_image_name}:{elasticsearch_version}")

    def __pull_mongodb_if_not_exists(self):
        mongodb_version: int = database_settings.mongo_settings.version
        mongodb_docker_image_name: str = database_settings.mongo_settings.name
        image.pull_if_not_exists(f"{mongodb_docker_image_name}:{mongodb_version}")

    def __run_postgres_if_pulled(self):
        postgres_settings = database_settings.postgres_settings
        container.run_if_exists_and_not_running(database_settings=postgres_settings)

    def __run_redis_if_pulled(self):
        redis_settings = database_settings.redis_settings
        container.run_if_exists_and_not_running(database_settings=redis_settings)

    def __run_mongodb_if_pulled(self):
        mongodb_settings = database_settings.mongo_settings
        container.run_if_exists_and_not_running(database_settings=mongodb_settings)

    def __run_elasticsearch_if_pulled(self):
        elasticsearch_settings = database_settings.elasticsearch_settings
        container.run_if_exists_and_not_running(database_settings=elasticsearch_settings)

    def pull_and_run(self):
        self.__pull_postgres_if_not_exists()
        self.__pull_redis_if_not_exists()
        self.__pull_elasticsearch_if_not_exists()
        self.__pull_mongodb_if_not_exists()
        self.__run_postgres_if_pulled()
        self.__run_redis_if_pulled()
        self.__run_mongodb_if_pulled()
        self.__run_elasticsearch_if_pulled()