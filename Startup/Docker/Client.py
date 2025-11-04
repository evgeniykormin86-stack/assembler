import docker
from docker.errors import NotFound

class Client:
    def __init__(self):
        # Connect to local Docker daemon via Unix socket
        self.__client = docker.from_env()
        self.__error_NotFound = NotFound

    @property
    def networks(self):
        return self.__client.networks

    @property
    def volumes(self):
        return self.__client.volumes

    @property
    def images(self):
        return self.__client.images

    @property
    def containers(self):
        return self.__client.containers

    @property
    def error_NotFound(self):
        return self.__error_NotFound
