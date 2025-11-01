import requests


class CISA(object):
    @staticmethod
    def get_cisa_kev(page_number: int, items_per_page: int) -> dict:
        return requests.get(
            f'https://kevin.gtfkd.com/kev?page={page_number}&per_page={items_per_page}'
        ).json()
