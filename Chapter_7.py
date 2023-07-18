message = input("Tell me something, and I will repeat it back to you: ")
print(message)

message = "If you tell us what you are, we can personaalize the messages you see"
message += "\nWhat is your first name?"

name = input(message)
print(name)

#Python takes inputs and list them as strings. In order to make them a number you need to do the following
age = input("How old are you?")
age = int(age)
print(age >= 18)

height = input("how tell are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou are not old enough to ride the ride")

#kind of random to throw this in here during chapter 7 but the modulo operator - divide two numbers and spit the remainder

print(5 % 3)

#While Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Letting the user quit a program
message = ("\nTell me something, and I will repeat it back to you: ")
message += "\n Type 'quit' to end the program "

prompt = ""
while prompt != 'quit':
   prompt = input(message)

   if prompt != 'quit':
       print("prompt")

####Flags
message = ("\nTell me something, and I will repeat it back to you: ")
message += "\n Type 'quit' to end the program "
active = True

while active:
    prompt = input(message)

    if prompt == 'quit':
        active = False
    else:
        print(prompt)

#break Command
prompt = "\nPlease enter the name of a city you have visted:"
prompt += "\n(Ehnter 'quit' when you are finished)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

###Using while loops with dictionsaries
unconfirmed_users = ['alice', 'brian', 'joe']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying users: {current_users.title()}")
    confirmed_users.append(current_users)

print("\n The following users have been confirmed:")
for confirmed_userss in confirmed_users:
    print(confirmed_userss.title())

#removing items
pets = ["dogs", "cat", "bird", "lion", "cat", "cat", "cat"]
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Filling a dictionary

responses = {}

#set a polling flag
polling_flag = True

while polling_flag:
    name = input("\n What is your name?")
    response = input("which mountain would you like to climb one day?")

#store the name and response
    responses[name] =response

#repeat the polling?
    repeat = input("would you like to let another personal respond? (yes/no)")

    if repeat == 'no':
        polling_flag = False
##Remeber the indentation matters in python. The statement below is outside the while loop
print("\n-----Polling Results")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
