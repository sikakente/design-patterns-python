from .abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print(f"The American Bull: Chevy Volt {2:c} prances into action")

    def stop(self):
        print(f"The American Bull: Chevy Volt {2:c} comes to a screeching halt!!")
