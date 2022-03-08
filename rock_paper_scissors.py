# put functions outside of loop
# function for user choice
def convert_user_choice(user_choice):
    if user_choice == 'R':
        user_choice = 'rock'
    elif user_choice == 'P':
        user_choice = 'paper'
    elif user_choice == 'S':
        user_choice = 'scissors'
    return user_choice

# put imports outside of loop
import random

# function for comp choice
def convert_comp_choice(comp_choice):
    if comp_choice == 0:
        comp_choice = 'rock'
    elif comp_choice == 1:
        comp_choice = 'paper'
    elif comp_choice == 2:
        comp_choice = 'scissors'
    return comp_choice

# function to determine winner
def game(user_choice, comp_choice):
    if user_choice == comp_choice:
        outcome = 'You have drawn!'
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (
            user_choice == 'paper' and comp_choice == 'rock') or (user_choice == 'scissors' and comp_choice == 'paper'):
        outcome = 'You have won!'
    elif (user_choice == 'rock' and comp_choice == 'paper') or (
            user_choice == 'paper' and comp_choice == 'scissors') or (
            user_choice == 'scissors' and comp_choice == 'rock'):
        outcome = 'You have lost :(.'
    return outcome

answer = input('Would you like to play rock paper scissors? (yes/no) ')
while answer == 'yes':
    user_choice = input("Enter R, P or S for rock, paper or scissors: ")
    # Call on my function here
    user_choice = convert_user_choice(user_choice)

    comp_choice = random.randint(0, 2)
    # Call on my function here
    comp_choice = convert_comp_choice(comp_choice)

    # Call on my game function here
    outcome = game(user_choice, comp_choice)

    print(outcome, 'You chose', user_choice, 'and the computer chose', comp_choice,)
    answer = input('Would you like to play again? ')

else:
    print('The game has now ended.')