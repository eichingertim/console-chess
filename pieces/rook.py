from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class Rook(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.ROOK, color)

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

    def check_move_for_direction(self, direction, des_pos, cur_pos, board):
        # #
        # if (des_col > cur_col and des_row == cur_row ):
        #     # right
            # for i in range(cur_col, des_col + 1):
            #         if (board.get_board()[des_row][i] != Empty()):
            #             if board.get_board()[des_row][i].get_color() != self.color:
            #                 if i == des_col:
            #                     return True
            #                 else:
            #                     return False
            #             else: 
            #                 return False
            #     return True
        # else if (des_col < cur_col and des_row == cur_row):
        #     # left
        # else if (des_row < cur_row and des_col == cur_col):
        #     # top
        # else if (des_row > cur_row and des_col == cur_col):
        #     # bottom
        # return false
        pass
