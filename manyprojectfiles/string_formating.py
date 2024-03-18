# String Formatting
# تنسيق النصوص بالطريقة القديمة
# Placeholder => العنصر النائب
# you must know first Every time when we modify the string, Python Always create a new String and assign a new string to that variable.

name = " Ahmed Khaled Mohamed Aboshenishen"
age = 24
rank = 20

print("My Full name is : %s , My age is : %d and Rank is : %f" % (name, age, rank))

number = 10
print("number is : %d" % number)
print("number is : %f" % number)
print("number is : %.3f" % number)
print("number is : %.2f" % number)

# %s => String
# %d => number
# %f => floating number

# Truncate String
message = "Hello peoples amy name is Ahmed And i happy to see my app"
print("message is : %s" % message)
print("message is : %.5s" % message)
print("message is : %.12s" % message)
print("message is : %.15s" % message)

name1 = "Ahmed Aboshenishen"
age1 = 24
rank1 = 100

print("name is : {} , my age is : {} and my rank in the world is : {}".format(name1, age1, rank1))
print("name is : {:s} , my age is : {:d} and my rank in the world is : {:f}".format(name1, age1, rank1))

# {:s} => String
# {:d} => number
# {:f} => floating number

message1 = "Hello peoples amy name is Ahmed And i happy to see my app"
print("message is : {:s}".format(message1))
print("message is : {:.5s}".format(message1))
print("message is : {:.12s}".format(message1))
print("message is : {:.15s}".format(message1))

# formatting money

MyMoney = 500162365004

print("My Money in my bank is : {:d} ".format(MyMoney))
# print("My Money in my bank is : {:_d} ".format(MyMoney))
print("My Money in my bank is : {:,d} ".format(MyMoney))

# rearrange Number
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Numbers is One Two Three
print("Hello {2} {1} {0}".format(a, b, c))  # Numbers is Three Two One
print("Hello {1} {0} {2}".format(a, b, c))  # Numbers is Two One Three

x, y, z = 20, 30, 50
print("numbers {} {} {}".format(x, y, z))
print("numbers {2} {0} {1}".format(x, y, z))
print("numbers {2:d} {0:d} {1:d}".format(x, y, z))
print("numbers {2:d} {0:d} {1:f}".format(x, y, z))
print("numbers {2:f} {0:f} {1:f}".format(x, y, z))
print("numbers {2:.2f} {0:.3f} {1:.5f}".format(x, y, z))

name2 = "Ahmed"
age2 = 24

print("My name is : {name2} and my age is : {age2}")
print(f"My name is : {name2} and my age is : {age2}")  # the Secret in f at first
