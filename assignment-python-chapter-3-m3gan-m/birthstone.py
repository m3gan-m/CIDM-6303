# Follow the assignment instructions to code an app that
# will tell a user their birthstone.
print("HW 3 - Megan Moore")
print()
user_input = ""
while True:
    user_input = input("Enter the number of the month you were born (1-12) or 'quit' >")
    if user_input == "1":
        stone = "Garnet"
        print("Your Birthstone is ", stone)
    elif user_input == "2":
        stone = "Amethyst"
        print("Your Birthstone is ", stone)
    elif user_input == "3":
        stone = "Aquamarine"
        print("Your Birthstone is ", stone)
    elif user_input == "4":
        stone = "Diamond"
        print("Your Birthstone is ", stone)
    elif user_input == "5":
        stone = "Emerald"
        print("Your Birthstone is ", stone)
    elif user_input == "6":
        stone = "Pearl"
        print("Your Birthstone is ", stone)
    elif user_input == "7":
        stone = "Ruby"
        print("Your Birthstone is ", stone)
    elif user_input == "8":
        stone = "Peridot"
        print("Your Birthstone is ", stone)
    elif user_input =="9":
        stone = "Sapphire"
        print("Your Birthstone is ", stone)
    elif user_input == "10":
        stone = "Opal"
        print("Your Birthstone is ", stone)
    elif user_input == "11":
        stone = "Citrine"
        print("Your Birthstone is ", stone)
    elif user_input == "12":
        stone = "Topaz"
        print("Your Birthstone is ", stone)
    elif user_input.lower() == "quit":
        break
print("*"*30)