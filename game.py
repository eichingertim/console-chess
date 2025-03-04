from board import Board
from player import Player
from pieces.color import Color
from helper.utils import Utils
from pieces.piece_type import PieceType

class Game:

    START_MESSAGE = """
    ###########################################################
    ################ Python Console Chess '21 #################
    ###########################################################

    Welcome to a complete Console-Chess-Interface. Feel free to
    try it, and have fun :D

    """

    def __init__(self):
        self.moves = list()
        self.player_white, self.player_black = None, None
        self.board = Board()
        self.winner = None
        self.is_check = False
        self.last_move_color = Color.BLACK

    def start_message(self):
        print(Game.START_MESSAGE)

        while (inp := input("    Enter 'START' to start the game: ")).lower() != 'start':
            print("    Wrong command!")

    def read_player(self):
        pb_name = input("    Enter the name of player BLACK: ")
        pw_name = input("    Enter the name of player WHITE: ")

        self.player_black = Player(pb_name, Color.BLACK)
        self.player_white = Player(pw_name, Color.WHITE)
    
    def start_game(self):

        self.start_message()
        self.read_player()

        while not self.board.is_game_over:

            print(self.board)

            if self.is_check:
                print(f"\n    {self.player_black if self.last_move_color == Color.WHITE else self.player_white}, you are in check")

            if self.last_move_color == Color.BLACK:
                print(f"    It's your turn {self.player_white}")
                self.last_move_color = self.move(self.player_white)
            else:
                print(f"    It's your turn {self.player_black}")
                self.last_move_color = self.move(self.player_black)

            self.is_check = self.board.check_for_check(self.last_move_color)

            self.board.is_game_over = self.board.check_for_check_mate(self.last_move_color)
        
        self.print_end()

    def print_end(self):

        print(self.board)

        if self.last_move_color == Color.WHITE:
            print(f"    Congratulations {self.player_white.name}! You won by checkmate.")
        else:
            print(f"    Congratulations {self.player_black.name}! You won by checkmate.")                
    
    def move(self, player):
        move_input = input("    Enter your move (e.g. A8 to A5): ")
        while not (val_result := Utils.is_valid_move(player, self.board, move_input.upper())).b:
            print(val_result.error)
            move_input = input("    Enter your move (e.g. A8 to A5): ")
        
        s_pos, e_pos = val_result.start_pos, val_result.end_pos
        
        self.board.move(s_pos, e_pos)


        # Checks if pawn transformation is possible
        if (e_pos[0] == 0 or e_pos[0] == 7) and self.board.get_type(e_pos) == PieceType.PAWN:
            piece_input = input("    Choose between ROOK, BISHOP, KNIGHT of QUEEN: ")
            while (piece_input != "ROOK" and piece_input != "BISHOP" and \
                piece_input != "KNIGHT" and piece_input != "QUEEN"):
                print("    This input is not valid")
                piece_input = input("    Choose between ROOK, BISHOP, KNIGHT of QUEEN: ")
            print(piece_input)
            self.board.set_piece(piece_input, player.color, e_pos)
                

        return player.color

