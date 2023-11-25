from .abs_factory import AbsFactory
from autos.ford_f150 import FordF150


class FordFactory(AbsFactory):
    def create_auto(self):
        self.ford = ford = FordF150()
        ford.name = "Ford F150"
        return ford
