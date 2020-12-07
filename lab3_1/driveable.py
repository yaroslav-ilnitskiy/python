from abc import ABC


class Driveable(ABC):

    def accelerate(self):
        pass

    def turn(self, side):
        pass

    def brake(self):
        pass
