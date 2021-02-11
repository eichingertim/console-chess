from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color
from .empty import Empty

class Knight(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.KNIGHT, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265E"
        else:
            return "\u2658"

    def can_move(self, board, dest_row, dest_col):

        cur_row, cur_col = board.get_position(self) 

        # Checks if destination position is current position
        if (cur_col, cur_row) == (dest_row, dest_col):
            return False

        if self.valid_move(cur_row, cur_col, dest_row, dest_col):
            piece_at_pos = board.board[dest_row][dest_col]
            if isinstance(piece_at_pos, Empty):
                return True
            else:
                return piece_at_pos.get_color() != self.get_color()

        
        return False
        

    def valid_move(self, cur_row, cur_col, dest_row, dest_col):
        return (abs(cur_row - dest_row) == 2 and abs(cur_col - dest_col) == 1) \
            or (abs(cur_row - dest_row) == 1 and abs(cur_col - dest_col) == 2)