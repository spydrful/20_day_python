#python uses square brackets for lists []

bycycles = (["trek", "redline", "knockooff", "electrical"])
print(bycycles)

#To access an item in the list you use index -a lot like powershell. Index starts at 0
print(bycycles[1])

#combine methods
print(bycycles[1].title())

#to grab the lsat letter in  the list you -1
print(bycycles[-1])

#Remember you use {} for inline text
message = f"My first bicycle was a {bycycles[1].title()}"
print(message)

#Changing an item in a list
motocycles = ['hoonda', 'yamaha', 'suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)

#Adding to the end of a list
motocycles.append('ducati')
print(motocycles)

#To add an item anywhere in a list use the .insert
motocycles.insert(0, 'BMW')
print(motocycles)

#remove an item from a list
del motocycles[1]
print(motocycles)

#Pop method basically pops the last value out of a list. However it can store that value
popped_motorcycle = motocycles.pop()
print(motocycles)
print(popped_motorcycle)

#if items were stored in order of being purchased you can do the following
last_owned = motocycles.pop()
print(f'The last motocycle I owned was a {popped_motorcycle.title()}')

#remove an item by value - Note that it only removes the first value it finds. A loop will be needed to remove the rest
too_expensive = 'BMW'
motocycles.remove(too_expensive)
print(motocycles)
print(f'Removing {too_expensive.title()} because it is too expensive')

#Lets say we want to sort a list in alphabetical order. This is permanent and cannot be reversed
cars = ['BMW', 'Honda', 'Toyota', 'Ford', 'Chevy']
cars.sort()
print(cars)

#you can also reverse the order
cars.sort(reverse=True)
print(cars)

#finding the length of a list
print(len(cars))
