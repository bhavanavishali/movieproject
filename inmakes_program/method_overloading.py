class Student:
     def sum(self,a=None,b=None,c=None):
           s=0
           if a!= None and b!= None and c!= None:
                 s = a+b+c
                 return s
           elif a!= None and b!= None:
                 s = a+b
                 return s
           else:
                 s = a 
                 return s

s1 = Student()
print(s1.sum(10,20,5))  

# exp1


class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
result1 = calc.add(1)
result2 = calc.add(1, 2)
result3 = calc.add(1, 2, 3)

# Print the results
print("Result 1:", result1)  # Output: 1
print("Result 2:", result2)  # Output: 3
print("Result 3:", result3)  # Output: 6
