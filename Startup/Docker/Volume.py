from Startup.Docker.Client import Client, NotFound


client = Client()


class Volume(object):
    def __create_volume(self, name: str):
        exists = client.volumes.create(name)
        return exists

    def __check_if_volume_exists(self, name: str):
        try:
            client.volumes.get(name)
            return True
        except NotFound:
            return False

    def create_if_not_exists(self, name: str):
        if not self.__check_if_volume_exists(name):
            self.__create_volume(name)
            return {'result': f'volume {name} created'}
        else:
            return {'result': f'volume {name} already exists'}
