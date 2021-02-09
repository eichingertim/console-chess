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

    # def can_move_to(self, board, des_row, des_col):

        # TODO: implement board.get_position()
        # TODO: implement borad.get_board()
        # TODO: implement borad.get_Board().get_color()
        # cur_row = board.get_position(self)[0]
        # cur_col = board.get_position(self)[1]
        # #
        # if (des_col > cur_col and des_row == cur_row ):
        #     # right
        # else if (des_col < cur_col and des_row == cur_row):
        #     # left
        # else if (des_row < cur_row and des_col == cur_col):
        #     # top
        # else if (des_row > cur_row and des_col == cur_col):
        #     # bottom
        # return false