from .abs_auto import AbsAuto


class NullCar(AbsAuto):
    def start(self):
        print(f"Unknown Car: {self.name}")

    def stop(self):
        print(f"Unknown Car: {self.name}")
