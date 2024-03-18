MyListFriend = ["Ahmed", "John", "Smith", "Ali"]
print(MyListFriend)
MyListFriend.append("Mohamed")
MyListFriend.append(100)
MyListFriend.append(150.215)
MyListFriend.append(True)
print(MyListFriend)
MyListFriend.append(["True", "False ", 50])
print(MyListFriend[8][1])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ["a", "b", "c", "d"]

a.extend(b)
print(a)
