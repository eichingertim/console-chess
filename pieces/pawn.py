from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class Pawn(BasePiece):

    # TODO oder vllt wo anders diese sondermethode?
    moved = False

    def __init__(self, color):
        super().__init__(PieceType.PAWN, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265F"
        else:
            return "\u2659"
            
    #TODO Schlagen
    #TODO Bauernumwandlung
    #TODO en passant

    def can_move(self, board, des_row, des_col):

        cur_row, cur_col =  board.get_position(self)

        # Checks if destination is current position
        if (cur_col, cur_row) == (des_row, des_col):
            return False

        # Checks if direction is allowed regarding their color
        if (self.color == Color.BLACK and des_row - cur_row > 0) or \
            (self.color == Color.WHITE and cur_row -des_row > 0):
            return False
        
        # Chacks if movement is not to far,(but does not include double movement check) 
        if (abs(cur_col - des_col) > 1 or abs(cur_row - des_row) > 2):
            return False
        
    def check_move_for_direcion(self, direction, des_pos, cur_pos, board):
        pass