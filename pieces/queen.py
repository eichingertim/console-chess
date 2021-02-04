from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class Queen(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.QUEEN, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265B"
        else:
            return "\u2655"

