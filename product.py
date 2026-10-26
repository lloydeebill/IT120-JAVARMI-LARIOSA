import Pyro5.api

@Pyro5.api.expose
class Product:
    def __init__(self, name: str, description: str, price: float):
        self._name = name
        self._description = description
        self._price = price

    def getName(self) -> str:
        return self._name

    def getDescription(self) -> str:
        return self._description

    def getPrice(self) -> float:
        return self._price