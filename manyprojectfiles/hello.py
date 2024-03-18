# new line \n
print("Hello World!\n\"ahmed khaled\"")
# carriage return \r
print("1234567\rAbcdE")

# concatenation
msg = "I love"
lang = "python"

print(msg + " " + lang)
final = msg + " " + lang
print(final)

# Strings

name = 'my name is "Ahmed khaled"'

value = '''hello this 
me i love 'good luck'
to meet you "nice to meet you"
'''
print(name)
print(value)

# index access item

first = "I love python so much"
print(first[0])  # will print "I"
print(first[9])  # will print "t"
print(first[-6])  # will print "o"

# slicing (Access Multiple sequence items)
print(first[14:16])  # will print th chars from char number 14 to 15
print(first[10:])  # will print from char number 10 to the end
print(first[:10])  # will print from char number 0 to number 10

print(first[0::1])  # full data
print(first[::1])  # full data
print(first[::2])  # from first char and take space 2 char
print(first[::1])  # from first char and take space 1 char
print(first[::3])  # from first char and take space 3 char
