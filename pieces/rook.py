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

