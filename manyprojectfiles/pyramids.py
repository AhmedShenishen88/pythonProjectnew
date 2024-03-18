# pyramids shape
# Define the height of the pyramid
height = 5

# for pyramids from bottom to top do the same code but add this
# for I in reversed(range(height)):
# alternative this for i in range(height):

for i in range(height):
    # Print leading spaces (for pyramid shape)
    print(" " * (height - i - 1), end="")

    # Inner loop to handle the number of asterisks in each row
    for j in range(2 * i + 1):
        print("*", end="")

    # Move to the next line after completing the row
    print()
