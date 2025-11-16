from Startup.Docker.Image import Image
from Startup.Docker.Container import Container
from Startup.Orchestrator.Settings import OrchestratorSettings


settings = OrchestratorSettings.load()
n8n_settings = settings.n8n
langflow_settings = settings.langflow

image: Image = Image()
container: Container = Container()


class Orchestrator(object):

    # -----------------------
    # PULL
    # -----------------------

    def __pull_n8n_if_not_exists(self):
        docker_image_name: str = n8n_settings.name
        docker_version: str = n8n_settings.version
        image.pull_if_not_exists(f"{docker_image_name}:{docker_version}")

    def __pull_langflow_if_not_exists(self):
        docker_image_name: str = langflow_settings.name
        docker_version: str = langflow_settings.version
        image.pull_if_not_exists(f"{docker_image_name}:{docker_version}")

    # -----------------------
    # RUN
    # -----------------------

    def __run_n8n_if_pulled(self):
        container.run_if_exists_and_not_running(database_settings=n8n_settings)

    def __run_langflow_if_pulled(self):
        container.run_if_exists_and_not_running(database_settings=langflow_settings)

    # -----------------------
    # N8N RUNNER
    # -----------------------

    def pull_and_run_n8n(self):
        self.__pull_n8n_if_not_exists()
        self.__run_n8n_if_pulled()

    # -----------------------
    # LANGFLOW RUNNER
    # -----------------------

    def pull_and_run_langflow(self):
        self.__pull_langflow_if_not_exists()
        self.__run_langflow_if_pulled()
