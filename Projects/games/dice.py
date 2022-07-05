import random
while True:
    possible_actions = ["1","2","3","4","5","6"]
    computer_action = random.choice(possible_actions)
    print(computer_action)
    print("Wanna Play Again (y/n) :- ")
    x=input()
    if x!="y":
        break
