import random
rand_num = random.randint(1, 100)

def main():
    score = 100
    while True : 
        user_guess = input('Guess number between 1and 100: ')

        if user_guess == 'q':
            print('Thank you for playing')
            break
        elif not user_guess.isdigit():
            print('Invalid input.Please try again.')
            score -= 5
            continue
        else:
            user_guess = int(user_guess)
            if user_guess > 100 or user_guess < 1:
                print('Your user guess is out of range. Please continue')
                score -= 5
                continue
            
            if rand_num > user_guess:
                print('Your guess is low')
                score -= 2
                continue
            elif rand_num < user_guess:
                print('Your guess is high')
                score -= 2
                continue
            else:
                print(f'well done your guess is true, random number was {rand_num} and your score is {score}')
                break


if __name__ == '__main__':
    main()