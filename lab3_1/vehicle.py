from driveable import Driveable

class Vehicle(Driveable):

    def __init__(self, gas_tank, engine, wheels):
        self.gas_tank = gas_tank
        self.engine = engine
        self.wheels = wheels.get_count()
        self.speed = 0

    def get_wheels_count(self):
        if self.wheels == 0:
            print("Not wheels")
        else:
            print('Count wheels ' + str(self.wheels))

    def accelerate(self):
        self.speed = self.speed + self.gas_tank.get()
        print('Speed up to  ' + str(self.speed) + 'km/hour')

    def turn(self, side):
        print('Turn to ' + str(side))

    def brake(self):
        while self.speed != 0:
            self.speed = self.speed - (self.speed / 2)
            if self.speed == 1:
                self.speed = 0
                break
            print('Speed: ' + str(self.speed) + 'km/hour')
            break
        print('Stop')
