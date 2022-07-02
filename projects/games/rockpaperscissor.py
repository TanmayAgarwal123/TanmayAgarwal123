import random
win=0
lose=0
tie=0
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        tie=tie+1
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            win=win+1
        else:
            print("Paper covers rock! You lose.")
            lose=lose+1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            win=win+1
        else:
            print("Scissors cuts paper! You lose.")
            lose=lose+1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            win=win+1
        else:
            print("Rock smashes scissors! You lose.")
            lose=lose+1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("wins - ",win)
        print("loses - ",lose)
        print("ties - ",tie)
        break