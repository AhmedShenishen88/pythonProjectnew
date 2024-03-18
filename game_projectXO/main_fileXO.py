class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name for game please your name is only letters ")
            if name.isalpha():  # isalpha for check if the letters is string or not
                self.name = name
                print(name)
                break
            print("Invalid name ,Please enter Letters only")

    def choose_symbol(self):
        while True:
            symbol = input(f"Hello {self.name} Enter your Symbol for game Only one letter please. ")
            print("Thanks")
            if symbol.isalpha() and len(symbol) == 1:  # isalpha for check if the letters is string or not and (len) for length of letter
                self.symbol = symbol.upper()
                break
            print("Invalid symbol ,Please enter one Letter only. ")
