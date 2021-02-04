from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class King(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.KING, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265A"
        else:
            return "\u2654"
