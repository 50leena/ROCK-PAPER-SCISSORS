import random

def play_game():
    # List of possible choices
    choices = ['rock', 'paper', 'scissors']
    print('Welcome to Rock, Paper, Scissors!')

    while True:
        # Get user input and handle exit condition
        user_choice = input('Choose rock, paper, or scissors (or type "quit" to exit): ').lower()
        if user_choice == 'quit':
            print('Thanks for playing!')
            break
        
        # Validate user input
        if user_choice not in choices:
            print('Invalid choice. Please try again.')
            continue

        # Computer randomly selects a choice
        computer_choice = random.choice(choices)
        print(f'Computer chose: {computer_choice}')

        # Determine the result based on game rules
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print('You win!')
        else:
            print('You lose!')

# Start the game
play_game()

