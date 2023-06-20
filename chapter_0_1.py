# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


name = "josh wallace"
print(name.title())
print(name.upper())
print(name.lower())

#Use two vairables in strings
first_name = "josh"
last_name = "wallace"
full_name = f"{first_name} {last_name}"
print(full_name)

#You can use F strings to write and format
message = f"hello, {full_name.title()}!"
print(message )

#Adding Whitespace
print("Python")
print("\tPython")

#NewLines
print("Languages:\nPython\nC\nJavascrpt")

#Striping whitespace out on thr right side. use lstrip() for left or strip() for all whitespace
favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

#Numbers
print(2-4)
print(4*8)
print(2+2)
print (3 ** 2)
print (2+3*4)

# Floats
print(0.2 + 0.1)

#Kind of a cool feature of python is that is can break  up large numbers
universe_age = 14_000_000_000_000
print(universe_age)

#Another cool feature is being able to assign mutiple variables at once
x, y, z = 4, 2, 5
print(x, y, z)

#Python doesn't have constants but if you want to set a varaibles that never change capitalize it
MAX_CONNECTIONS = 500

# The zen of pythong
import this
