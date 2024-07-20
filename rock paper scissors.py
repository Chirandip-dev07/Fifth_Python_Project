print("WELCOME TO ROCK PAPER SCISSORS GAME :) ")
print("PLEASE ENTER INPUTS IN CAPITAL LETTERS")
print(" ")
print("ENJOY IT AND BEAT THE COMPUTER")

turns = int(input("PLEASE ENTER THE NUMBER OF TURNS YOU WANT : "))
moves = ['ROCK','PAPER','SCISSORS']
import random
user_point = 0
comp_point = 0
for i in range(turns):
    user_choice = input("WHAT DO YOU WANNA GO FOR (ROCK/PAPER/SCISSORS)? : ")
    comp_choice = random.choice(moves)

    if user_choice == "ROCK":
        if comp_choice == "PAPER":
            print("COMPUTER'S MOVE IS PAPER")
            print("COMPUTER WINS")
            comp_point = comp_point + 1
        elif comp_choice == "SCISSORS":
            print("COMPUTER'S MOVE IS SCISSORS")
            print("YOU WIN")
            user_point = user_point + 1
        else:
            print("COMPUTER'S MOVE IS ROCK")
            print("IT'S A TIE")

    elif user_choice == "SCISSORS":
        if comp_choice == "ROCK":
            print("COMPUTER'S MOVE IS ROCK")
            print("COMPUTER WINS")
            comp_point = comp_point + 1
        elif comp_choice == "PAPER":
            print("COMPUTER'S MOVE IS PAPER")
            print("YOU WIN")
            user_point = user_point + 1
        else:
            print("COMPUTER'S MOVE IS SCISSORS")
            print("IT'S A TIE")

    elif user_choice == "PAPER":
        if comp_choice == "SCISSORS":
            print("COMPUTER'S MOVE IS SCISSORS")
            print("COMPUTER WINS")
            comp_point = comp_point + 1
        elif comp_choice == "ROCK":
            print("COMPUTER'S MOVE IS ROCK")
            print("YOU WIN")
            user_point = user_point + 1
        else:
            print("COMPUTER'S MOVE IS PAPER")
            print("IT'S A TIE")

    else:
        print("WRONG CHOICE ENTERED :(")

print("END OF GAME :) ")
print("CALCULATING RESULTS...............")
print(" ")
print("THE SCORE IS")
print(" COMPUTER : ",comp_point)
print(" YOU : ",user_point) 
if user_point>comp_point:
    print("CONGRATULATIONS! YOU WON THE GAME")
elif user_point<comp_point:
    print("ALAS! COMPUTER WON THE GAME")
    print("WELL TRIED, BETTER LUCK NEXT TIME")
else:
    print("SCORES MATCHED, IT IS A TIE")
print(" ")
print("THANKS FOR PLAYING THE GAME")
