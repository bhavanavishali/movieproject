class Sample:
    def __init__(self,name) -> None:
        self.name = name
    def __add__(self,other):
        name = self.name+other.name
        return name
    

first_name = Sample('bhavana ')
second_name = Sample('vishali')
full_name = first_name+second_name
print(full_name)