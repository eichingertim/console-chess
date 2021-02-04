from base_piece import BasePiece
from piece_type import PieceType

class King(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.KING, color)
