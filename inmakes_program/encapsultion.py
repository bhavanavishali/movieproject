class Payment:
    def __init__(self, price) -> None:
        self.__price = price + price * 0.5

    def get_finalprice(self):
        return self.__price
    def set_finalprice(self,dist):
        self.__price = self.__price - self.__discount(dist)
    def __discount(self,dist):
        return  self.__price*(dist/100)

    


b1 = Payment(52)
b1.set_finalprice(20)
print(b1.get_finalprice())
