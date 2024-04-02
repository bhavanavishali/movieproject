# class Student:
#     def __init__(self,school) -> None:
#         self.name = 'nimi'
#         self.rollnumber = 55
#         self.school = school
#     def putdata(self):
#         self.school = input('Enter the school name')

#     def getdata(self):
#         print(self.name)
#         print('school name is:',self.school)
# obj1=Student('')
# obj1.putdata()
# obj1.getdata()

# obj2 = Student('lsn')
# obj2.putdata()
# obj2.getdata()
        
# class Computer:
#     def __init__(self) -> None:
#         self.name = 'bhavana'
#         self.age = 50
#     def update(self):
#         print('age is',self.age)

# ob1 =Computer()
# ob2 =Computer()


# print(ob1.name)
# ob2.update()

# .................variable in oops............

class Car:

    wheel = 4       #class variable

    def __init__(self) -> None:
        self.mil = 10
        self.com = 'BMW'        #instance variable
    
c1= Car()
c2= Car()
c1.mil = 20

Car.wheel = 5

print(c1.mil,c1.com,c1.wheel)
print(c2.mil,c2.com,c2.wheel)
 

# .................methods  in oops............

class Student:

    school = 'LSN'

    def __init__(self,name,m1,m2,m3) -> None:
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        print('name is',self.name)
        self.avg = (self.m1+self.m2+self.m3)/3
        print('average is:',self.avg)

    @classmethod
    def getschool(cls):
        print('school name is :',cls.school)

    @staticmethod
    def info():
        print("this is staatic method multiple class")


s1 = Student('kukku',40,20,80)
s1.avg()
Student.getschool()
Student.info()

#..............inner class .....................

class Student:
    def __init__(self,name,rollno) -> None:
         self.name = name
         self.rollno = rollno
         self.lap1 = self.Laptop('HB')   #innerclass object(lap1)


    def show(self):
        print('name is :',self.name)
        print('rollno :',self.rollno)
        self.lap1.show()    #call method of innerclass

    class Laptop:
        def __init__(self,brand) -> None:
             self.brand = brand
        def show(self):
            print('laptop brand :',self.brand)

s1= Student('amu',10)
s1.show()