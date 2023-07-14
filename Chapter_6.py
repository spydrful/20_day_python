#Chatper 6 Dictionaires

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Dictionaries are basically built in XML. Its a way to store key-pair data

new_points = alien_0['points']
print(f'Your just earned {new_points} points!')

#addin new key pair values
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0["points"] = 5

print(alien_0)

#Modifying values
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0}")

alien_0['color'] = 'yellow'
print(f"the alien is now {alien_0['color']}")


#Tracking the position
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points': '5'}
print(f"original position: {alien_0['x_position']}")

#move the alien to the right.
#Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"new position:{alien_0['x_position']}")

#Remove a key pair
del alien_0['points']
print(alien_0)

#Similar Objects
favorite_languages = {
    'jen': 'python',
    'sara': 'c',
    'james': 'ruby',
    'josh': 'c#',
}

language = favorite_languages['jen'].title()
print(f"jn's favorite language is: {language}")

#To fail gracefully
point_valie = alien_0.get('points', 'No point value assigned')
print(point_valie)

#############################################
#Looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages.values():
    print(name.title())

#####NESTING#######
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 5}

aliens = [alien_0, alien_2, alien_1]

for alien in aliens:
    print(alien)


print(f"\n Below is the start of the range method")

aliens = []

#Make 30 aliens
for alien_number in range(30):
    new_alien = {'color': "green", 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

    for alien in aliens[:3]:
        if alien['color'] == "green":
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")

####Showhow man aliens have been created.
print(f'Total number of aliens: {len(aliens)}')

print("\n A list in a dictionary")
pizaa = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizaa['crust']}-crust pizza with the following toppings:")

for toppings in pizaa['toppings']:
    print(f"\t{toppings}")