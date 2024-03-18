def validate_choice():
    while True:
        choice = int(input("Enter your choice: from 1 or 2 \n"))
        if choice == 1 or choice == 2:
            return choice
        print("Invalid Choice ,Please try again")


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
            if symbol.isalpha() and len(
                    symbol) == 1:  # isalpha for check if the letters is string or not and (len) for length of letter
                self.symbol = symbol.upper()
                break
            print("Invalid symbol ,Please enter one Letter only. ")


class Menu:
    def display_main_menu(self):
        print("Welcome to the game x o ")
        print("Please Choose one of the of these symbol")
        print("1. for Start Game ")
        print("2. for End Game ")
        validate_choice()

    def display_end_game(self):
        menu_text = """ 
Game Over!
1. Restart Game
2. Quit Game
Enter your choice: 1 or 2 ,please
        """
        print(menu_text)
        validate_choice()


# t1 = Menu()
# t1.display_main_menu()
# t1.display_end_game()
