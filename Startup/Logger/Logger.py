from Startup.Docker.Image import Image
from Startup.Docker.Container import Container
from Startup.Logger.Settings import LoggerSettings
import os
import secrets


image = Image()
container: Container = Container()
logger_settings = LoggerSettings.load()


class GrayLog(object):
    def __pull_graylog_if_not_exists(self):
        graylog_docker_image_name: str = logger_settings.GrayLog.name
        graylog_version: str = logger_settings.GrayLog.version
        return image.pull_if_not_exists(f"{graylog_docker_image_name}:{graylog_version}")

    def __run_graylog_if_pulled(self):
        graylog_settings = logger_settings.GrayLog
        return container.run_if_exists_and_not_running(database_settings=graylog_settings)

    def __create_graylog_secret_key(self):
        if not os.path.exists("GRAYLOG_SECRETS.txt"):
            GRAYLOG_SECRETS = ''.join(
                secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32))
            with open("GRAYLOG_SECRETS.txt", 'w') as file:
                file.write(GRAYLOG_SECRETS)

    def pull_and_run(self):
        self.__create_graylog_secret_key()
        self.__pull_graylog_if_not_exists()
        self.__run_graylog_if_pulled()
