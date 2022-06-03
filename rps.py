import random


class Player:
    moves = ["rock", "paper", "scissors"]

    def __init__(self):
        self.score = 0
        self.user_move = self.moves
        self.computer_move = random.choice(self.moves)

    def learn(self, user_move, computer_move):
        self.user_move = user_move
        self.computer_move = computer_move


class RockPlayer(Player):
    def move(self):
        return self.moves[0]


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ImitatePlayer(Player):
    def move(self):
        return self.computer_move


class CyclePlayer(Player):
    def move(self):
        if self.user_move == self.moves[0]:
            return self.moves[1]
        elif self.user_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            user_choice = input("Rock, Paper or Scissors? ... ")
            if user_choice.lower() in self.moves:
                return user_choice.lower()
            elif user_choice.lower() == "quit":
                quit()


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if beats(move1, move2):
            self.p1.score = 1
            display = "--- YOU Win! ---"
        elif beats(move2, move1):
            self.p2.score = 1
            display = "--- COMPUTER Wins! ---"
        else:
            display = "--- Tie! ---"
        print(
            f"--- YOU played: {move1}"
            f"\n--- COMPUTER played: {move2}"
            f"\n{display}"
            f"\nScoreboard:"
            f"\nYOU ( {self.p1.score} ),"
            f" COMPUTER ( {self.p2.score} )"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4, 1):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(
                f"\n--- YOU Won the Game! ---"
                f"\nYOU ( {self.p1.score} ),"
                f" Computer ( {self.p2.score} )"
            )
        elif self.p1.score == self.p2.score:
            print(
                f"\n--- No Winner This Time! ---"
                f"\nYOU ( {self.p1.score} ),"
                f" COMPUTER ( {self.p2.score} )"
            )
        else:
            print(
                f"\n--- COMPUTER Won the Game! ---"
                f"\nYOU ( {self.p1.score} ),"
                f" COMPUTER ( {self.p2.score} )"
            )


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RockPlayer(), RandomPlayer(), ImitatePlayer(), CyclePlayer()]))
    game.play_game()
