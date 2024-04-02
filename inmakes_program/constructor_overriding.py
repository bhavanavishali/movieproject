class superclass:
    def __init__(self) -> None:
        print("super class init")

class subclass(superclass):
    def __init__(self) -> None:
        super().__init__()
        print('subclass init')

s1 = subclass()