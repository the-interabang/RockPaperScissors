# rock paper scissors game
from ResultsGrid import GridGen


def rock_paper_scissors():
    input1 = input("User 1, type rock, paper, or scissors: ")
    input2 = input("User 2, type rock, paper, or scissors: ")
    print("user input received")
    input1 = input1.lower()
    input2 = input2.lower()

    if "rock" == input1:
        if "scissors" == input2:
            print("Player 1 wins!")
        elif "paper" == input2:
            print("Player 2 wins!")
        elif "rock" == input2:
            print("It's a draw. You both win!")
        else:
            print("You didn't follow the instructions")
    elif "paper" == input1:
        if "scissors" == input2:
            print("Player 2 wins!")
        elif "rock" == input2:
            print("Player 1 wins!")
        elif "paper" == input2:
            print("It's a draw. You both win!")
        else:
            print("You didn't follow the instructions")
    elif "scissors" == input1:
        if "paper" == input2:
            print("Player 2 wins!")
        elif "rock" == input2:
            print("Player 1 wins!")
        elif "scissors" == input2:
            print("It's a draw. You both win!")
        else:
            print("You didn't follow the instructions")
    else:
        print("You didn't follow the instructions. Goodbye")
    check_yes_no()

#this will take users' input
def user_pick():
    user1 = input("Player 1, type 'rock', 'paper', or 'scissors': ")
    user2 = input("Player 2, type 'rock', 'paper', or 'scissors: ")

#this will evaluate who won
def winner():
    grid = GridGen()

#this will check whether users want to play again
def check_yes_no():
    yes_no = input("Would you you like to play again? Type Yes or No: ")
    yes_no = yes_no.lower()
    if yes_no == "yes":
        rock_paper_scissors()
    elif yes_no == "no":
        print("Have a good day! Bye :)")
    else:
        print("You didn't follow the instructions. Goodbye")


rock_paper_scissors()
