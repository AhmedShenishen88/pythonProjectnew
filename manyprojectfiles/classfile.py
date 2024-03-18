class MyClass:
    def __init__(self, items):
        self.items = items

    def print_items(self):
        for item in self.items:
            print(item)


# Calling the class in another place
if __name__ == "__main__":
    items_to_print = ["apple", "banana", "cherry", "date"]
    my_object = MyClass(items_to_print)
    my_object.print_items()

# __name__ is a special variable in Python that contains the name of the current module.
# When Python runs a script, it sets the special variable __name__ to '__main__' if the script is being executed directly.
# The if __name__ == "__main__": statement allows you to ensure that certain code only runs when the script is executed directly,
# not when it's imported as a module into another script.
x = -5

if x > 0:
    print("x is bidder and Positive")
elif x == 0:
    print("x is Zero")
else:
    print("x is negative")
