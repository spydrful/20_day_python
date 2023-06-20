#loops - A lot like powershell

magicians = ['alive', 'david', 'carolina']
for magician in magicians:
        print(magician)

magicians = ['alive', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    #Don't forget that indentation matters in python. It doesn't in powershell. See the difference below

magicians = ['alive', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n") #This  isn't part of the loop

#Making Numerical Lists
for value in range(1,5): #python starts counting at the first number you give it
    print(value)

for value in range(6):
    print(value)

#concert Ranges of numbers in to a list by wrapping it
numbers = list(range(2, 11))
print(numbers)

#You can also set the step by which numbers are added
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#Square numbers in a list
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#A quicker way to do the above would e
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

#Finding the MIN MAX and SUM of a list
digits = list(range(10))
print(min(digits))
print(max(digits))
print(sum(digits))

#list Comprehension- Begin with a name, followed by expression, for loop
squares = [value**2 for value in range(1,11)]
print(squares)

#slicing a list to work in parts
players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[0:3])

print("Here are the firsrt three players on my team:")
for player in players[:3]:
    print(player.title())

#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("My friends favorite foods are:")
print(friends_foods)

my_foods.append("cannoli")
friends_foods.append("ice cream")
print(my_foods)
print(friends_foods)

#note that setting my_foods = friends_foods does not create two different lists. If you append to one it appends to the other

#if you want to create an immutable list you use what python calls tuples
#you use () instead of []

square_block = (200, 50)
print(square_block)

####Throws an error
#square_block[0] = 1000
#print(square_block)

#However that doesn't mean we can't overwrite the variable.
square_block = (100, 200, 300)
print(square_block)