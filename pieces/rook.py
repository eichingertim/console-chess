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

        # TODO: implement board.get_position()
        # cur_row = board.get_position(self)[0]
        # cur_col = board.get_position(self)[1]
        # cur_row = board.get_position(self)
        # cur_col = board.get_position(self)

        # return can_move_to(self, board, des_row, des_col, cur_row, cur_col)
        pass

    def can_move_to(self, board, des_row, des_col):
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
