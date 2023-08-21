# Follow the instructions for how to code this application
#Megan Moore
guest_list = []
user_input= ""

while True:
    user_input=input("Enter a guest's name or type or 'end' to stop.\n")
    if user_input.lower() != "end":
        guest_list.append(user_input)
    elif user_input.lower() == "end":
        count = len(guest_list)
        totalcost = 12.00*count
        total="%.2f" % totalcost
        print(*guest_list, sep = "\n")
        print(f"You have invited ",count," at a cost of $",total,".")
        break
print("*"*30)