from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class Pawn(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.PAWN, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265F"
        else:
            return "\u2659"
