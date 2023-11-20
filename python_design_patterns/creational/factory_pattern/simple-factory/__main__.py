from autofactory import AutoFactory

carnames = ['MaseratiLevante', 'ChevyVolt', 'MercedesSClass']

factory = AutoFactory()

for carname in carnames:
    car = factory.create_instance(carname)
    car.start()
    car.stop()
