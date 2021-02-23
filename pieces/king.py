from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color
from .empty import Empty
import operator

class King(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.KING, color)
        self.is_moved = False

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
        if (abs(dest_row - cur_row) <= 1 and abs(dest_col - cur_col) <= 1):
            piece_at_pos = board.board[dest_row][dest_col]
            if isinstance(piece_at_pos, Empty):
                return True
            else:
                return piece_at_pos.get_color() != self.get_color()

        # Check special turn "Rochade"
        if not self.is_moved:
            if ((cur_col - dest_col == 3 or dest_col - cur_col == 2) and dest_row-cur_row == 0):
                direction = -1 if dest_col - cur_col < 0 else 1
                for distance in range(1, (abs(dest_col - cur_col)+1)):
                    move = (0, distance * direction)
                    new_pos = tuple(map(operator.add, (cur_row, cur_col), move))
                    piece_at_pos = board.board[new_pos[0]][new_pos[1]]
                    if isinstance(piece_at_pos, Empty):
                        if new_pos == (dest_row, dest_col):
                            return True
                    else:
                        return False
        
        return False