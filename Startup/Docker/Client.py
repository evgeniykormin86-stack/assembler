from docker import DockerClient
from docker.errors import NotFound


class Client(object):
    def __init__(self):
        self.__client: DockerClient = DockerClient(base_url='tcp://localhost:2375')
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
