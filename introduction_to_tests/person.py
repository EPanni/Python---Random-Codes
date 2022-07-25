import requests


class Person:
    def __init__(self, name: str, surname: str, data=False) -> None:
        self.name = name
        self.surname = surname
        self.data = data

    def retrieve_data(self):
        response = requests.get("fake_url")

        if response.ok:
            self.data = True
            return "CONNECTED"
        else:
            return "ERROR 404"
