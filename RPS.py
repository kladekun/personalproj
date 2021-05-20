import random 
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while(1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    userChoiceR = input("Choose your weapon [R]ocks\, [P]aper, or [S]cissors: ")
    userChoice = userChoiceR[0]
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter: ")
        print ("[R]ock, [S]cissors or [P[aper.")
        continue
    print ("You chose: " + userChoice)
    choices = ['R', 'P','S']
    opponentChoice = random.choice(choices)
    print ("I chose: " + opponentChoice)
    if opponentChoice == str.upper(userChoice):
        print ("Tie!")
    #if opponentChoice == str("R') and str.upper(userChoice) == "P"
    elif opponentChoice == 'S' and userChoice.upper() == 'R':
        print ("Rocks beats Scissors, I win!")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'S':
        print ("Scissors beat Paper, I win!")
        continue
    elif opponentChoice == 'R' and userChoice.upper() == 'P':
        print ("Paper beat Rock, I win!")
        continue
    else:
        print ("You LOSE HAHAHAHAHA!")
