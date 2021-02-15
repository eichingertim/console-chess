from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color
from .empty import Empty

class King(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.KING, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265A"
        else:
            return "\u2654"

    def can_move(self, board, dest_row, dest_col):

        cur_row, cur_col = board.get_position(self) 

        # Checks if destination position is current position
        if (cur_col, cur_row) == (dest_row, dest_col):
            return False

        # Check the move
        if (abs(dest_row - cur_row) <= 1 or abs(dest_col - cur_col) <= 1):
            piece_at_pos = board.board[dest_row][dest_col]
            if isinstance(piece_at_pos, Empty):
                return True
            else:
                return piece_at_pos.get_color() != self.get_color()
        
        return False