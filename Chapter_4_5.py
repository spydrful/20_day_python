cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

## A single = sign means to set a variable to that value. A double == means to compare the two values
#Testing for equality is case sensitive so Audi does not equal audi

car.lower() == 'audi'

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Checking values - Seeing if a list contains an item
requested_topping = ["mushrooms", 'onions', 'pineapple']
print('mushrooms' in requested_topping)

#Checking if a user is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#Using Booleans you can use = true
# if conditional_test:
#   do something

#Else if statements
#age = 19
age = 17
if age >= 18:
    print("you are old enough to vote")
else:
    print("Sorry , you are too young to vote")
    print("Please Register to vote as soon as you turn 18!")

#mutiple else if chain
age = 12
test = 14

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your Admission cost is $40")

#The last else is not required but is useful

requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print('Adding Mushrooms')
if 'pepperoni' in requested_topping:
    print('Adding pepperoni')
if 'extra cheese' in requested_topping:
    print('Adding extra cheese')

print("\nFinished making your pizza!")

#Using if statements with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#Updated
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#Using Mutiple lists
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
availble_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', "pineapple", 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availble_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry, wed don't have {requested_topping}")

print("\nFinished making your pizza")