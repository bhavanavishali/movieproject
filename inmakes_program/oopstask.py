
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(12):
    print(fibonacci(i))


# inheritance

class Vehicle:
    def __init__(self) -> None:
        self.price = 45000
        self.company = 'maruti'

class Car(Vehicle):
    def four_wheel(self):
        print(self.company)
        print('car have four wheels')
    
class Bike(Vehicle):
    def two_wheel(self):
        print(self.price)
        print('bike have two wheel')

b1 = Bike()
b1.two_wheel()

c1=Car()
c1.four_wheel()





