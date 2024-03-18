# height = 10
#
# for i in reversed(range(height)):
#     print(" " * (height - i - 1), end="")
#
#     for j in range(2 * i + 1):
#         print("*", end="")
#
#     print()
#
# num_sum = 0
# info = 0.0
# for i in range(1, 11):
#     Num = float(input("Enter your Number ".format(i)))
#
#     num_sum = num_sum + Num
#
# print("your sum of your Number is : ", num_sum)

a = "I love python"
print(len(a))


name = "    I love You     "
print(name.strip())
print(name.rstrip())
print(name.lstrip())

name = "#@##@#@# I love You #@#@#@#@#"
print(name.strip('#@'))
print(name.rstrip('@#'))
print(name.lstrip('@#'))


shape = "hello my name is ahmed khaled mohamed aboshenishen my age is 24 years old"
print(shape.title())
print(shape.upper())
print(shape.capitalize())

a, b, c, d = "1", "10", "111", "1231"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))

height = 10


for i in range(height):
    print(" " * (height - i - 1), end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()

for i in reversed(range(height)):
    print(" " * (height - i - 1), end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()