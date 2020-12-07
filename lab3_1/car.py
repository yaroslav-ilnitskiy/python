from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, gas_tank, engine, wheels):
        super(Car, self).__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print('Speed car ' + str(self.speed))
        super(Car, self).accelerate()

    def turn(self, side):
        print('Car turn')
        super(Car, self).turn(side)

    def brake(self):
        super(Car, self).brake()
        print('Car stop')

    def get_wheels_count(self):
        super(Car, self).get_wheels_count()
