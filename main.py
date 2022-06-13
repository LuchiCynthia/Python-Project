import random

print("posible_options.")
print("R rock")
print("P paper")
print("S scissors")

while True :
    user_action = input("Enter a choice(R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. Its a tie!, repeat action")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smahes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
            
        break

    else: 
        user_action == "invalide"
        print("Error! repeat action")
