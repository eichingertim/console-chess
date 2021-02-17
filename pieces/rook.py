from .base_piece import BasePiece
from .piece_type import PieceType
from .empty import Empty
from .color import Color
import operator

class Rook(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.ROOK, color)
        self.is_moved = False

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265C"
        else:
            return "\u2656"     

    def can_move(self, board, des_row, des_col):

        cur_row, cur_col = board.get_position(self)

        # Checks if destination position is current position
        # or is not a horizontal/vertical movement
        # TODO (reihenfolge wichtig?)
        if ((cur_col - des_col) != 0 and (cur_row - des_row) != 0) \
            or (cur_col, cur_row) == (des_row, des_col):
            return False

        # calculates the direction for move
        direction = (1 if cur_row - des_row < 0 else -1 if des_row - cur_row < 0 else 0, \
            1 if cur_col - des_col < 0 else -1 if des_col - cur_col < 0 else 0)
        # -1 left/up
        # 1 right/down
            
        return self.check_move_for_direction(direction, \
            (des_row, des_col), (cur_row, cur_col), board)

    # goes through all fields in the given direction and checks if 
    # the piece can move to this point
    def check_move_for_direction(self, direction, des_pos, cur_pos, board):
        for distance in range(1, 8):
            move = (distance * direction[0], distance * direction[1])
            new_pos = tuple(map(operator.add, cur_pos, move))
            if board.is_valid_pos(new_pos):
                piece_at_pos = board.board[new_pos[0]][new_pos[1]]
                if isinstance(piece_at_pos, Empty):
                    if (new_pos == des_pos):
                        return True
                else:
                    if piece_at_pos.color == self.color:
                        return False
                    else:
                        return new_pos == des_pos
            else:
                return False
        return False
