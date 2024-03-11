import random

VALID_CHOICES = ['r', 'p', 's', 'l', 'Sp']
FULL_NAMES = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'l': 'lizard', 'Sp': 'Spock'}

def prompt(message):
    print(f"==> {message}")

# Find a winner adding lizard and spock    
def display_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        prompt('It"s a tie!')
        return 'tie'
    elif (user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or \
         (user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'Spock')) or \
         (user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or \
         (user_choice == 'lizard' and (computer_choice == 'Spock' or computer_choice == 'paper')) or \
         (user_choice == 'Spock' and (computer_choice == 'scissors' or computer_choice == 'rock')):
        prompt('You win!')
        return 'You win!'
    else:
        prompt('Computer wins!')
        return 'Computer wins!'
        
def keep_score():
    # keep score until player or computer wins 5 times
    player_score = 0
    computer_score = 0
    
    while player_score < 5 and computer_score < 5:
        # ask user to choose between rock, paper, scissors
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}, :  Type r for rock, p for paper, s for scissors, l for lizard, Sp for Spock')
        choice = input()

        while choice not in VALID_CHOICES:
            prompt('Invalid choice. Choose one: r, p, s, l, Sp')
            choice = input()

        # computer chooses between rock, paper, scissors
        computer_choice = random.choice(VALID_CHOICES)

        # display the choices
        prompt(f'You chose {choice}, the computer chose {computer_choice}')

        # determine the winner
        result = display_winner(FULL_NAMES[choice], FULL_NAMES[computer_choice])
        
        if result == 'You win!':
            player_score += 1
        elif result == 'Computer wins!':
            computer_score += 1
        prompt(f'Player score: {player_score}, Computer score: {computer_score}')
        
    if player_score == 5:
        prompt('You win the game!')
    else:
        prompt('Computer wins the game!')
        
keep_score()