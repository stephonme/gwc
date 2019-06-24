start = '''
You are lost in the woods with your bestfriend and you must make it out alive'''

keepplaying= "yes"
print(start)

while keepplaying == "Yes" or keepplaying == "yes":
    userchoice= input ("Will you take the dark scary path or the candy covered one? Type 1 for the dark scary path. Type 2 for the candy path.")
    if userchoice == "1":
        print ("You have found a witch who claims could help you get home")
        print("She trasnports you to your home with a single spell" )
        print ("You end up deeper in the woods however.")
        print("")
        keepplaying = "no"
    elif userchoice == "2":
        print("The candy path gives you plenty of food to survive for the next three weeks")
        print("Unfortunetly you got stuck in the sticky caramel river")
        print("You will die a slow death")
        keepplaying = input ("Would you like to play again? Type yes or no.")
    else:
        print("Select one of the valid options: 1 or 2.")
        keepplaying= input ("Would you like to try again? Type yes or no.")
    if keepplaying == "no":
        quit()
keepplaying= "yes"
while keepplaying == "Yes" or keepplaying == "yes":
    userchoice = input ("This time you meet a wizard and he says he will transport you home will you trust him? Type trust or don't trust.")
    if userchoice == ("trust"):
        print("Congrats, he stuck to his promise and you are now home safe and sound.")
    elif userchoice == ("don't trust"):
        print("The wizard leaves you since you did not trust him")
        print("You will die alone in the woods.")
    else: 
        print("Please select one of the valid options: 1 or 2.")
        keepplaying= input ("Would you like to try again? Type yes or no.")
    if keepplaying == "no":
        quit()
    