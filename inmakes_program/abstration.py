from abc import ABC, abstractmethod
class Vehicle(ABC):
    def speed(self):
        print(' the speed')
    def apply_break(self):
        print('the break')
    @abstractmethod
    def gear(self):
        pass
        
class Car(Vehicle):
    def gear(self):
        print('change the gear automatically')

class Truck(Vehicle):
    def gear(self):
        print('change the gear mannully')

c1 = Car()
c1.gear()