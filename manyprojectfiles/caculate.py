number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

result = number1 + number2
print("The sum of", number1, "and ", number2, "is", result)

# for loop

total_sum = 0
for i in range(0, 10):
    num = float(input("Enter your numbers : ".format(i)))
    total_sum = total_sum + num
print("The sum of the 10 numbers is:", total_sum)

# pyramids shape
height = 10
for i in range(height):
    # Print leading spaces (for pyramid shape)
    print(" "*(height - i - 1), end="")

    # Inner loop to handle the number of asterisks in each row
    for j in range(2 * i + 1):
        print("*", end="")

    # Move to the next line after completing the row
    print()

