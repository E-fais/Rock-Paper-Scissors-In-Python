import random
prompts = [
    'A)ROCK', 'B)PAPER', 'C)SCISSSORS'
]
user_guesses_options = ["A", "B", "C"]


def start_game():
    score = 0
    computer_score = 0
    attempts = 0

    print('ROCK PAPER SCISSORS\n***************')
    while attempts < 3:  # adjusted attempts to 3
        attempts += 1
        for prompt in prompts:
            print(prompt)
        user_guess = input('Enter Your guess as A,B or C \n : ').upper()
        # get index of computer guess
        computer_guess = round(random.random() * 2)

        # Print guesses based on indexes to display the same values for both user and computer
        print(
            f"Your guess: {prompts[user_guesses_options.index(user_guess)]} , Computer guess : {prompts[computer_guess]}")
        if user_guess not in user_guesses_options:
            print('Invalid response, Reply with A, B OR C Only!!')
            continue  # Skip invalid responses

        # Get index of user guess
        user_guess_index = user_guesses_options.index(user_guess)

        # Compare both index based on their value
        if user_guess_index == computer_guess:
            print("That is tie")
        elif user_guess_index == 0 and computer_guess == 2:
            score += user_win(score)
        elif user_guess_index == 1 and computer_guess == 0:
            score += user_win(score)
        elif user_guess_index == 2 and computer_guess == 1:
            score += user_win(score)
        else:
            print('Computer wins and gets one score!')
            computer_score += 1
    result(score, computer_score)


def user_win(score):
    print(f'You get one score !! your total score: {score + 1}')
    return 1


def result(score, computer_score):
    print(
        f'Game Over Your Score is {score} and computer score= {computer_score}')
    if score > computer_score:
        print('CONGRATULATIONS YOU WON')
    elif score == computer_score:
        print('THAT IS A TIE!')
    else:
        print('TRY AGAIN YOU LOSE!')


start_game()
