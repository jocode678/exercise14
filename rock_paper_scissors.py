answer = input('Would you like to play rock paper scissors? (yes/no) ')
while answer == 'yes':
    user_choice = input("Enter R, P or S for rock, paper or scissors: ")

    if user_choice == 'R':
        user_choice = 'rock'
    elif user_choice == 'P':
        user_choice = 'paper'
    elif user_choice == 'S':
        user_choice = 'scissors'
    # print(user_choice)

    import random

    comp_choice = random.randint(0, 2)
    # print(comp_choice)

    if comp_choice == 0:
        comp_choice = 'rock'
    elif comp_choice == 1:
        comp_choice = 'paper'
    elif comp_choice == 2:
        comp_choice = 'scissors'


    # print(comp_choice)

    def game(user_choice, comp_choice):
        if user_choice == comp_choice:
            outcome = 'You have drawn!'
        elif user_choice == 'rock' and comp_choice == 'scissors':
            outcome = 'You have won!'
        elif user_choice == 'rock' and comp_choice == 'paper':
            outcome = 'You have lost :(.'
        elif user_choice == 'paper' and comp_choice == 'rock':
            outcome = 'You have won!'
        elif user_choice == 'paper' and comp_choice == 'scissors':
            outcome = 'You have lost :(.'
        elif user_choice == 'scissors' and comp_choice == 'rock':
            outcome = 'You have lost :(.'
        elif user_choice == 'scissors' and comp_choice == 'paper':
            outcome = 'You have won!'
        return outcome


    outcome = game(user_choice, comp_choice)

    print(outcome, 'You chose', user_choice, 'and the computer chose', comp_choice, )
    answer = input('Would you like to play again? ')

else:
    print('The game has now ended.')