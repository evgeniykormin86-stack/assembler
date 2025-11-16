from Startup.Docker.Client import Client, NotFound
import hashlib


client = Client()


class Container(Client):
    def run_if_exists_and_not_running(self, database_settings) -> None:
        container_details = self.__get_container_details(container_name=database_settings.name)
        container = container_details['container']
        if container is not None:
            container.reload()
        if container_details['if_exists']:
            print(f'Container {database_settings.name} exists')
            if container_details['status'] == 'running':
                print(f'Container {database_settings.name} is running')
            else:
                print(f'Container {database_settings.name} is not running')
                container = container_details['container']
                print(f'Container {database_settings.name} start')
                container.start()
        else:
            print(f'Container {database_settings.name} does not exist')
            if database_settings.name == 'postgres':
                self.__run_postgres_container(database_settings)
            elif database_settings.name == 'redis':
                self.__run_redis_container(database_settings)
            elif database_settings.name == 'mongo':
                self.__run_mongodb_container(database_settings)
            elif database_settings.name == 'elasticsearch':
                self.__run_elasticsearch_container(database_settings)
            elif database_settings.name == 'assembler-python-sdk':
                self.__run_assembler_python_sdk_if_pulled(database_settings=database_settings)
            elif database_settings.name == 'graylog/graylog':
                self.__run_graylog_if_pulled(database_settings=database_settings)
            elif database_settings.name == 'n8nio/n8n':
                self.__run_n8n_if_pulled(database_settings=database_settings)

    @staticmethod
    def __get_container_details(container_name: str):
        try:
            container = client.containers.get(container_name.replace('/', '_'))
            return {
                "container": container,
                "if_exists": True,
                "status": container.status
            }
        except NotFound:
            return {
                "container": None,
                "if_exists": False,
                "status": None
            }

    @staticmethod
    def __run_postgres_container(database_settings):
        client.containers.run(
            f'{database_settings.name}:{database_settings.version}',
            name=database_settings.name,
            detach=True,
            environment=database_settings.environment,
            ports=database_settings.ports,
            network=database_settings.network,
            volumes=database_settings.volumes
        )

    @staticmethod
    def __run_redis_container(database_settings):
        client.containers.run(
            f'{database_settings.name}:{database_settings.version}',
            name=database_settings.name,
            detach=True,
            ports=database_settings.ports,
            network=database_settings.network,
            volumes=database_settings.volumes
        )

    @staticmethod
    def __run_mongodb_container(database_settings):
        client.containers.run(
            f'{database_settings.name}:{database_settings.version}',
            name=database_settings.name,
            detach=True,
            ports=database_settings.ports,
            network=database_settings.network,
            volumes=database_settings.volumes
        )

    @staticmethod
    def __run_elasticsearch_container(database_settings):
        client.containers.run(
            f'{database_settings.name}:{database_settings.version}',
            name=database_settings.name,
            detach=True,
            environment=database_settings.environment,
            ports=database_settings.ports,
            network=database_settings.network,
            volumes=database_settings.volumes
        )

    @staticmethod
    def __run_assembler_python_sdk_if_pulled(database_settings):
        client.containers.run(
            image=f'{database_settings.name}:{database_settings.version}',
            name=database_settings.name,
            detach=True,
            ports=database_settings.ports,
            environment=database_settings.environment,
            network=database_settings.network,
            volumes=database_settings.volumes
        )

    @staticmethod
    def __run_graylog_if_pulled(database_settings):
        PASSWORD: str = database_settings.environment['password']
        sha256 = hashlib.sha256(PASSWORD.encode()).hexdigest()

        # Read the secret from file
        with open('GRAYLOG_SECRETS.txt', 'r') as f:
            GRAYLOG_SECRET_KEY = f.read().strip()  # remove trailing newline

        client.containers.run(
            image=f'{database_settings.name}:{database_settings.version}',
            name=database_settings.name.replace('/', '_'),
            detach=True,
            ports=database_settings.ports,
            environment={
                "GRAYLOG_PASSWORD_SECRET": GRAYLOG_SECRET_KEY,  # <-- variable, not string
                "GRAYLOG_ROOT_PASSWORD_SHA2": sha256,
                "GRAYLOG_HTTP_EXTERNAL_URI": "http://127.0.0.1:9000/",
                "GRAYLOG_ELASTICSEARCH_HOSTS": "http://elasticsearch:9200"
            },
            network=database_settings.network,
            volumes=database_settings.volumes
        )

    @staticmethod
    def __run_n8n_if_pulled(database_settings):
        print(database_settings)
        client.containers.run(
            image=f'{database_settings.name}:{database_settings.version}',
            name=database_settings.name.replace('/', '_'),
            detach=True,
            ports=database_settings.ports,
            environment=database_settings.environment,
            network=database_settings.network,
            volumes=database_settings.volumes
        )