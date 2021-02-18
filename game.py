from board import Board
from player import Player
from pieces.color import Color
from helper.utils import Utils
from pieces.piece_type import PieceType

class Game:

    def __init__(self):
        self.moves = list()
        self.player_white, self.player_black = None, None
        self.board = Board()
        self.winner = None
        self.last_move_color = Color.WHITE

    def read_player(self):
        pb_name = input("Enter the name of player BLACK: ")
        pw_name = input("Enter the name of player WHITE: ")

        self.player_black = Player(pb_name, Color.BLACK)
        self.player_white = Player(pw_name, Color.WHITE)
    
    def start_game(self):
        self.read_player()

        while not self.board.is_game_over:

            print(self.board)

            if self.last_move_color == Color.BLACK:
                print(f"It's your turn {self.player_white}")
                self.last_move_color = self.move(self.player_white)
            else:
                print(f"It's your turn {self.player_black}")
                self.last_move_color = self.move(self.player_black)

            # self.winner = self.board.check_for_check_mate(self.last_move_color)
        
        self.print_end()

    def print_end(self):
        if self.last_move_color == Color.WHITE:
            print(f"Congratulations {self.player_white.name}! You won.")
        else:
            print(f"Congratulations {self.player_black.name}! You won.")                
    
    def move(self, player):
        move_input = input("Enter your move (e.g. A8 to A5): ")
        while not (val_result := Utils.is_valid_move(player, self.board, move_input)).b:
            print(val_result.error)
            move_input = input("Enter your move (e.g. A8 to A5): ")
        
        s_pos, e_pos = val_result.start_pos, val_result.end_pos

        self.board.move(s_pos, e_pos)


        # Checks if pawn transformation is possible
        if (e_pos[0] == 0 or e_pos[0] == 7) and self.board.get_type(e_pos) == PieceType.PAWN:
            piece_input = input("Choose between ROOK, BISHOP, KNIGHT of QUEEN: ")
            while (piece_input != "ROOK" and piece_input != "BISHOP" and \
                piece_input != "KNIGHT" and piece_input != "QUEEN"):
                print("This input is not valid")
                piece_input = input("Choose between ROOK, BISHOP, KNIGHT of QUEEN: ")
            print(piece_input)
            self.board.set_piece(piece_input, player.color, e_pos)
                

        return player.color

