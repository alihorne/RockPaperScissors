import random


def valid_input(prompt, options):

    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print('SORRY, THAT IS INVALID.PLEASE TRY AGAIN')

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self. my_move = ''
        self.their_move = ''

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self. my_move = my_move
        self. their_move = their_move


class Random_Player(Player):
    def move(self):
        return random.choice(moves)


class Learn_Player(Player):
        def move(self):
            return self.their_move

        def learnMoves(self, my_move, their_move):
            self.their_move = their_move
            self.my_move = my_move


# human input

class Human_Player(Player):
    def move(self):
        return valid_input("rock, paper, scissors?", moves)


class Rock_Player(Player):
    def move(self):
        return 'rock'


class Reflect_Player(Player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self. my_move = my_move
        self. their_move = their_move

# remembers what move it played last round


class Cycle_Player(Player):

    def __init__(self):
        self.my_next_move_index = random.randrange(3)

    def move(self):
        my_next_move = moves[self.my_next_move_index]
        self.my_next_move_index = (self.my_next_move_index + 1) % 3
        return my_next_move


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 : {move1}  Player 2 : {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score = self.p1_score + 1
            print("Player 1 WINS!!\n"
                  f"Player 1: {move1}  Player 2: {move2}\n"
                  f"Player_1 score:{self.p1_score}\n"
                  f"Player_2 score:{self.p2_score}")
            print(" ")

        elif beats(move2, move1):
            self.p2_score = self.p2_score + 1
            print("Player 2 WINS!!\n"
                  f"Player 1: {move1}  Player 2: {move2}\n"
                  f"Player_1 score:{self.p1_score}\n"
                  f"Player_2 score:{self.p2_score}")
            print(" ")

        else:
            print("Draw!")
            print(" ")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

# play game
    def play_game(self):
        print("Let's Play Rock Paper Scissors!\n")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()

        print(f'FINAL SCORE: Player One : {self.p1_score}'
              f'Player Two : {self.p2_score}\n')
        if self.p1_score > self.p2_score:
            print('Player 1 is the winner!')
            print("GAME OVER!!!")

        elif self.p2_score == self.p1_score:
            print('No WINNER! The game is a TIE!\n')

        else:
            print('The score is TIED. Next point WINS!')
            print(" ")
            while (self.p2_score == self.p1_score):
                print("FINAL Round")
                self.play_round()

            print("GAME OVER!!")


if __name__ == '__main__':

    players = [Cycle_Player(),
               Learn_Player(),
               Reflect_Player(),
               Random_Player(),
               Rock_Player()]
    p1 = Human_Player()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
