from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class Bishop(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.BISHOP, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265D"
        else:
            return "\u2657"
