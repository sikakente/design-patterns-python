from .abs_factory import AbsFactory
from autos.chevy_volt import ChevyVolt


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = "Chevy Volt"
        return chevy
