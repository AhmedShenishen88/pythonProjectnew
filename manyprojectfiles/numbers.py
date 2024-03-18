# we have int, float, complex (types)

# integer
num0 = 1
num1 = 10
num2 = -1
num3 = -31
print(type(num0))
print(type(num1))
print(type(num2))
print(type(num3))

# Float
numF0 = 1.001
numF1 = 10.15541
numF2 = -1.41
numF3 = -31.144
print(type(numF0))
print(type(numF1))
print(type(numF2))
print(type(numF3))

# complex contain two part real and imaginary
myComplexNumber = 10 + 5j
print(type(myComplexNumber))

print("myComplexNumber is: {}".format(myComplexNumber))
print("Real part is: {}".format(myComplexNumber.real))
print("Imaginary part is: {}".format(myComplexNumber.imag))

# [1] we can convert from int to float and complex
# [2] we can convert from float to int and complex
# [3] we cannot convert from complex to float and int

print(100)
print(float(100))
print(complex(100))
print(100.4)
print(int(100.4))
print(complex(100.4))

print(5+60j)
# print(int(5+60j))  => error
