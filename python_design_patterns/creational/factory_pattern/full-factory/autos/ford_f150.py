from .abs_auto import AbsAuto


class FordF150(AbsAuto):
    def start(self):
        print(f"{self.name} started!")

    def stop(self):
        print(f"{self.name} stopped!")
