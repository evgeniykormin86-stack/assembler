from Startup.Docker.Container import Container
from Startup.SDK.Settings import DatabaseSettings


database_settings = DatabaseSettings.load()
container: Container = Container()


class AssemblerPythonSDK(object):
    @staticmethod
    def run_assembler_python_sdk_if_pulled() -> None:
        assembler_python_sdk_settings = database_settings.SDK_settings
        container.run_if_exists_and_not_running(database_settings=assembler_python_sdk_settings)
