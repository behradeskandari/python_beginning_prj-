import random


class RockPaperScissers:
    def __init__(self, name):
        self.choice = ['rock', 'paper', 'scissers']
        self.player_name = name

    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choice}): ')
        if user_choice.lower() in self.choice:
            return user_choice.lower()
        
        print(f'Invalid choice you must select from {self.choice}')
        return self.get_player_choice()

    def get_computer_choice(self):
        return random.choice(self.choice)

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "it's Tie!"
        win_combinations = [('paper', 'rock'), ('scissors', 'paper'), ('rock', 'scissors')]
        
        for winner in win_combinations:
            if (user_choice == winner[0]) & (computer_choice == winner[1]):
                return f"congrats, {self.player_name} win!"
            else:
                return 'oh no!, computer won!'
        
    # play
    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(computer_choice)
        print(winner_msg)


if __name__ == '__main__':
    game = RockPaperScissers('Behrad')


while True:
    # game = RockPaperScissers('Behrad')
    game.play()
    continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
    if continue_game.lower() == 'q':
        break