##Chapter 8 Function!

#Simple functio to great a user
def greet_user():
    print("Hello, Hej da")

greet_user()

#passing a value to a function
def greet_user_v2(username):
    print(f"Hello, {username.title()}")

greet_user_v2("Josh")

def favorite_book(book):
    print(f"My favorite book is {book.title()}")
favorite_book("Name of the wind")

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet("Dog", "James Bond")

#If you want your code to be clearer to read you could use positional arguements
describe_pet(animal_type="cat", pet_name="Sara")

#you cal so mix them up by using animal_type, pet_name=jim

#Return Values
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jimi", "hendrix")
print(musician)

#Values don't always have to be required if you write code to catch them - check the null value
def get_formatted_name_optional(first_name, last_name, middle_name=''):
    if middle_name:
     full_name = f"{first_name} {middle_name} {last_name}"
    else:
     full_name = f"{first_name} {last_name}"

    return full_name.title()
musician = get_formatted_name_optional("jimi", "hendrix")
print(musician)

musician = get_formatted_name_optional("john", "hooker", "lee")
print(musician)