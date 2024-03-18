# salary = 8000

# def printSalary():
#     salary = 12000
#     print("Salary is :", salary)
#
#
# printSalary()
# print(salary)

# for i in range(10, 15, 1):
#     print(i, end=",")
# class Person:
#     def __init__(self, name, sex, profession, salary):
#         self.name = name
#         self.sex = sex
#         self.profession = profession
#         self.salary = salary
#
#     def show(self):
#         print(f"my name is : {self.name} , my gender is : {self.sex}, and")
#
#     def work(self):
#         print(f"I am working as : {self.profession}, My Salary is : {self.salary}", )
#
#
# jessa = Person("Jessa", "Female ", "Software Engineering", "10000$")
# Ahmed = Person("Ahmed", "Male ", "Software Engineering", "50000$")
#
#
# jessa.show()
# jessa.work()
# Ahmed.show()
# Ahmed.work()

# class Person:
#     def __init__(self, name, gender, profession, salary):
#         self.name = name
#         self.gender = gender
#         self.profession = profession
#         self.salary = salary
#
#     def show(self):
#         # print(f"my name is   {self.name}, my gender is {self.gender}")
#         print("My name is {} , and my gender is {}".format(self.name, self.gender))
#
#     def work(self):
#         print("I am working as ", self.profession, "and my salary is ", self.salary)
#
#
# p1 = Person("John", "Male", "Software Engineer", "5000$")
# p1.show()
# p1.work()


# class Student:
#     school_name = "ABC School"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# s1 = Student("John", 24)
#
# print("School Name: ", s1.school_name)
# print("Student Name:", s1.name)
# print("And Student Age :", s1.age)
#
# s2 = Student("jessa", 23)
# s2.school_name = "XYZ School"
# print("And The Second Inf of Student is ")
# print(f"School name is : {s2.school_name}  \nStudent Name is : {s2.name} \nAge is : {s2.age}")

# height = int(input("Give me you height of your pyramids : "))
#
# for i in range(height):
#     print(" "*(height-i-1), end="")
#
#     for j in range(2*i+1):
#         print("*", end="")
#
#     print()

# n1 = input("Enter Your First Name: ")
# print("Hello ", n1)
# n2 = input("Enter your last name ")
# print("so  ", n1.upper(), n2.upper())
# n3 = n1 + " " + n2
# a1 = input("Enter Your Age ")
# print(f"so Your name is {n3.upper()} and your age is {a1} right ")

# n1 = int(input("Enter your first number:  "))
# n2 = float(input("Enter your second number:  "))
# n3 = int(input("Enter your third number:  "))
#
# n4 = n1 + n2 + n3
# print("The sum of is: ", n4, "and the type of your result is ", type(n4))

#
# friends = ["Ahmed", "Mohamed", "Ahmed", "Khaled"]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list1 = [10, 20, True, ["Jessa", "Ali"]]
#
# print(friends[0])
# print(friends[5])
# print(friends[6])
# print(friends[6][1])
# print(friends[-1][0])
# print(friends[1:5])
# print(friends[1:5:1])
# print(friends[1:6:2])
# print(friends)
# friends[0] = "Islam"
# print(friends)
# friends.insert(0, "Ahmed")
# print(friends)
# last_variable = friends.pop()
# print(last_variable)
# print(friends)
# print(friends.count("Ahmed"))
# friends.sort()
# print(friends)

# tuples
# variable = (45, 55)
# print(variable)
# variable[0] = 80 error
# print(type(variable))
# print(variable[1])

# methods
# def say_hi(name, age, profession):
#     print("Hello", name.upper(), "your age is", age, "and your profession is", profession.upper())
#     # print("Hello" + name.upper() + "your age is" + age + "and your profession is" + profession.upper()) in integer make error
#     print("Right")
#
#
# name_user = input("Enter your name: ")
# age_user = input("Enter your Age: ")
# profession_user = input("Enter your Profession: ")
# say_hi(name_user, age_user, profession_user)
# say_hi("name_user", 24, "profession_user")

# def cube(num):
#     result = 1
#     for i in range(3):  # Multiplying the number by itself three times to get the cube
#         result *= num
#     return result
#
#
# # Example usage:
# number = int(input("Enter a number to find its cube: "))
# print("Cube of", number, "is", cube(number))

# def cube(num, i):
#     result = 1
#     for j in range(i):
#         result = result * num
#     return result
#
#
# number = int(input("Enter a number: "))
# Multiplying_number = int(input("Enter your  Multiplying number: "))
# cube_result = cube(number, Multiplying_number)
# print("Cube of", number, "is", cube(number, Multiplying_number))
height = 10

# for i in reversed(range(height)):
for i in range(height):
    print(" " * (height - i), end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()
