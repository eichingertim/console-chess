from base_piece import BasePiece
from piece_type import PieceType

class Bishop(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.BISHOP, color)
