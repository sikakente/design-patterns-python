from .abs_auto import AbsAuto


class MaseratiLevante(AbsAuto):
    def start(self):
        print(
            f"The italian stalion Maserati Levante {2:c} prances into action"
        )

    def stop(self):
        print(f"The italian stalion Maserati Levante {2:c} sleeps now")
