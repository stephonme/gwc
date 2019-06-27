# --- Define your functions below! ---


# --- Put your main program below! ---
def introduction():
        print("Whattup homie. I am thee chatbot.")

def game():
    choice = input("Choose either rock, paper, or scissors:")
    if choice == "rock":
        print("Ha! I chose paper, so you lose!")

        userChoice = input("Wanna play again?")
        if userChoice == "yes" or userChoice == "Yes":
            print(" ")
            print("Okay let's play!")
            game()
        elif userChoice == "no" or userChoice == "No":
            print(" ")
            print("Alright then be like that.")
            quit()

    elif choice == "paper":
        print("Ha I chose scissors, you lose!")

        userChoice = input("Wanna play again?")
        if userChoice == "yes" or userChoice == "Yes":
            print(" ")
            print("Okay let's play!")
            game()
        elif userChoice == "no" or userChoice == "No":
            print(" ")
            print("Alright then be like that.")
            quit()

    elif choice == "scissors":
        print("Ha I chose rock, you lose!")

        userChoice = input("Wanna play again?")
        if userChoice == "yes" or userChoice == "Yes":
            print(" ")
            print("Okay let's play!")
            game()
        elif userChoice == "no" or userChoice == "No":
            print(" ")
            print("Alright then be like that.")
            quit()



def rps():
    print("I bet you can't beat me in rock paper scissors!")
    print(" ")
    userChoice = input("Wanna play?")
    if userChoice == "yes" or userChoice == "Yes":
        print(" ")
        print("Okay let's play!")
        game()
    elif userChoice == "no" or userChoice == "No":
        print(" ")
        print("Alright then be like that.")
        quit()
    




def main():
    i = 1
    introduction()
    while  i == 1:
        answer = input("(What will you say?) ")
        if answer == "Hi" or answer == "hi":
            print(" ")
            print("Dope.")
            rps()

        elif answer == "Hello" or answer == "hello":
            print(" ")
            print("Dope.")
            rps()
        elif answer == "Whattup" or answer == "whattup":
            print(" ")
            print("Dope.")
            rps()

        else:
            print(" ")
            print("Wooowwwwww you aren't going to say hi back?")




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()