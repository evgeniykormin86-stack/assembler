from Startup.Docker.Client import Client, NotFound


client = Client()


class Image(object):
    def __pull_image(self, name: str):
        exists = client.images.pull(name)
        return exists

    def __check_if_image_was_pulled(self, name: str):
        try:
            client.images.get(name)
            return True
        except NotFound:
            return False

    def pull_if_not_exists(self, name: str):
        if not self.__check_if_image_was_pulled(name):
            print(f'Pulling <{name}>')
            self.__pull_image(name)
        else:
            print(f"Image <{name}> already pulled")
