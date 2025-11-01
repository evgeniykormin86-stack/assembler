from Startup.Docker.Client import Client, NotFound


client = Client()


class Network(object):
    def __init__(self, network_name: str):
        self.__network_name: str = network_name

    def __create_network(self):
        exists = client.networks.create(self.__network_name)
        return exists

    def __check_if_network_exists(self, name: str):
        try:
            client.networks.get(name)
            return True
        except NotFound:
            return False

    def create_if_not_exists(self):
        if not self.__check_if_network_exists(self.__network_name):
            self.__create_network()
