# Write code for tic tac toe 
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        print("\nCurrent board:")
        for i in range(3):
            print("|".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 5)
        print()

    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_full(self):
        return ' ' not in self.board

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def play_game(self):
        current_player = 'X' if random.choice([True, False]) else 'O'
        while True:
            self.print_board()
            if current_player == 'X':
                try:
                    position = int(input(f"Player {current_player}, enter your move (0-8): "))
                except ValueError:
                    print("Please enter a valid number between 0 and 8.")
                    continue
            else:
                position = random.choice(self.get_available_moves())
                print(f"Computer ({current_player}) chose position {position}")

            if position not in range(9):
                print("Invalid position. Choose a number between 0 and 8.")
                continue

            if self.make_move(position, current_player):
                if self.is_winner(current_player):
                    self.print_board()
                    print(f"Player {current_player} wins!")
                    break
                elif self.is_full():
                    self.print_board()
                    print("It's a draw!")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move, try again.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()