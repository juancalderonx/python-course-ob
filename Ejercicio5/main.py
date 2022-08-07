age = int(input('¡Hi! Please type your age '))

if age < 0:
    print("Error, invalid age")
elif age < 18:
    print("You're a minor")
else:
    print("You're a legal")
