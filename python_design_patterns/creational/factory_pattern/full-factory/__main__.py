from factories import loader
from autos.abs_auto import AbsAuto


for factory_name in "chevy_factory", "ford_factory", "tesla_factory":
    factory = loader.load_factory(factory_name)
    car: AbsAuto = factory.create_auto()

    car.start()
    car.stop()
