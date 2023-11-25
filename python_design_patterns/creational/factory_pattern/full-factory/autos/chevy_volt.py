from .abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print(f"{self.name} started!")

    def stop(self):
        print(f"{self.name} stopped!")
