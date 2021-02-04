from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class Knight(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.KNIGHT, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265E"
        else:
            return "\u2658"