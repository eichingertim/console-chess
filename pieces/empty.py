from .base_piece import BasePiece
from .piece_type import PieceType
from .color import Color

class Empty(BasePiece):

    def __init__(self):
        super().__init__(PieceType.EMPTY, None)

    def __str__(self):
        return " "