from .abs_auto import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, name) -> None:
        self._carname = name

    def start(self):
        print(f"Unknown car: {self._carname}")

    def stop(self):
        pass
