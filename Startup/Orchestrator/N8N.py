from Startup.Docker.Image import Image
from Startup.Docker.Container import Container
from Startup.Orchestrator.Settings import N8NSettings


n8n_settings = N8NSettings.load()
image: Image = Image()
container: Container = Container()


class N8N(object):
    def __pull_n8n_if_not_exists(self):
        n8n_docker_image_name: str = n8n_settings.N8N.name
        n8n_version: str = n8n_settings.N8N.version
        return image.pull_if_not_exists(f"{n8n_docker_image_name}:{n8n_version}")

    def __run_n8n_if_pulled(self):
        graylog_settings = n8n_settings.N8N
        return container.run_if_exists_and_not_running(database_settings=graylog_settings)

    def pull_and_run(self):
        self.__pull_n8n_if_not_exists()
        self.__run_n8n_if_pulled()
