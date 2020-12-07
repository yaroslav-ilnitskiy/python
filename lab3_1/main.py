from boat import Boat
from car import Car
from engine import Engine
from gas_tank import GasTank
from solar_car import SolarCar
from wheels import Wheels


def drive(driveable):
    driveable.get_wheels_count()
    driveable.turn('Right')
    driveable.accelerate()
    driveable.turn('Right')
    driveable.brake()


if __name__ == '__main__':
    car = Car(GasTank(60), Engine(80), Wheels(4))
    solarCar = SolarCar(GasTank(50), Engine(120), Wheels(8))
    boat = Boat(GasTank(900), Engine(200), Wheels(0))

    for i in [boat, car, solarCar]:
        drive(i)
