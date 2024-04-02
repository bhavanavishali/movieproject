# 1
# x = [10,'bhavana','python',200,30,45]
# new_list = ["my name is {} , i love {}".format(x[1],x[2])]
# print(new_list)
# # 2
# y = [10,25,30,41,50,66,70,80]
# print(y[2:6])
# #3
# ab = ('apple','avacado','mango','banana','orange','pineapple','strewberry')
# cd = list(ab)
# cd.insert(3,'blueberry')
# cd.append('cherry')
# ab =tuple(cd)
# print(ab)
# print(ab[-2])


# 2 (oops)

# class Hospital:
#     def hospital_details(self):
#         self.admin = input('enter the admin name :')
#         self.doctor = input('enter the doctor  name :')
#         self.sister = input('enter the sister name :')
#         self.department = input('enter the department name :')
# class Department(Hospital):
#     def display(self):
#         print('admin is ',self.admin)
#         print('Doctor is ',self.doctor)
#         print('Sister is ',self.sister)
#         print('Department  is ',self.department)

# class Patient:
#     def get_data(self):
#         print('patient details')
#         self.name = input('enter the patient name:')
#         self.age = int(input('enter the age:'))
#         self.diseases = input('enter the diseases:')
#     def display(self):
#         print('patient details:')
#         print(self.name)
#         print(self.age)
#         print(self.diseases)

# d1 = Department()
# p1 = Patient()

# d1.hospital_details()
# d1.display()
# p1.get_data()
# p1.display()

# 2 qus set

set1 = {1,22,8,7,34,20}
set1.add(5)
print(set1)
set2 = {'apple','orange','grapes'}
set1.update(set2)
print(set1)
set1.remove('apple')
print(set1)

x ={2,4,8}
y ={3,9,6}
z = x.union(y)
print(z)

a = {1,2,3,4}
b = {7,8,3,6}
c = a.intersection(b)
print(c)

