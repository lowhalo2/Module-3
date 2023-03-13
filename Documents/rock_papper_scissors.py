from random import randint

def draw(player_choice):
    # Choose rock paper or scissors and pass player_choice and computer_choice compare() to check
    options = ["rock", "paper", "scissor"]
    computer_choice = options[randint(0,2)]
    print(f"Computer choose {computer_choice}.")
    compare(player_choice, computer_choice)

# compares x to y and prints out either you win, you lose, or game tied
def compare(x, y):
    if x == 'rock':
        if y == 'paper':
            print('You lose.')
        elif y == 'scissor':
            print('You win.')
        else:
            print('Game Tied')
    elif x == 'paper':
        if y == 'scissor':
            print('You lose.')
        elif y == 'rock':
            print('You win.')
        else:
            print('Game Tied')
    else:
        if y == 'rock':
            print('You lose.')
        elif y == 'paper':
            print('You win.')
        else:
            print('Game Tied')

# player makes theire choice and if choice is rock paper or scissor it will be sent to draw()
# If choice is quit it will say thank you for playing and close the loop
running = True
print('Welcome to rock paper scissors!')
while running:
    choice = input('choose rock, paper, scissor, or quit:  ')
    if choice.lower() == 'rock':
        draw(choice)
    elif choice.lower() == 'paper':
        draw(choice)
    elif choice.lower() == 'scissor':
        draw(choice)
    elif choice.lower() == 'quit':
        running = False
        print('Thank you for playing!')