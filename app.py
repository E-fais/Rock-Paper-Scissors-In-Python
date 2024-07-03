import random
prompts = [
    'A)ROCK', 'B)PAPER', 'C)SCISSSORS'
]

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
        computer_guess = prompts[round(random.random() * 2)]
        print(f"Your guess: {user_guess} , Computer guess : {computer_guess}")
        if user_guess not in ["A", "B", "C"]:
            print('Invalid response, Reply with A, B OR C Only!!')
            continue  #Skip invalid responses
        if user_guess == computer_guess:
            print("That is tie")
        elif user_guess == 'A' and computer_guess == 'C)SCISSSORS':
            score += user_win(score)
        elif user_guess == 'B' and computer_guess == 'A)ROCK':
            score += user_win(score)
        elif user_guess == 'C' and computer_guess == 'B)PAPER': 
            score += user_win(score)
        else:
            print('Computer wins and gets one score!')
            computer_score += 1 
    result(score, computer_score)

def user_win(score):
    print(f'You get one score !! your total score: {score + 1}') 
    return 1

def result(score, computer_score):
    print(f'Game Over Your Score is {score} and computer score= {computer_score}')
    if score > computer_score:
        print('CONGRATULATIONS YOU WON')
    elif score==computer_score:
        print('THAT IS A TIE!')
    else:
        print('TRY AGAIN YOU LOSE!')

start_game()