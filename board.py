from pieces.base_piece import BasePiece
from pieces.color import Color
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.pawn import Pawn
from pieces.king import King
from pieces.empty import Empty
import numpy as np

class Board:

    LETTERS = [chr(i) for i in range(65, 73)]
    NUMBERS = [i for i in range(1, 9)]
    NUMBERS.reverse()

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        b = np.zeros((8,8), dtype=BasePiece)
        b[0] = [Rook(Color.BLACK), Knight(Color.BLACK), \
             Bishop(Color.BLACK), Queen(Color.BLACK), King(Color.BLACK), \
                 Bishop(Color.BLACK), Knight(Color.BLACK), Rook(Color.BLACK)]
        b[1] = [Pawn(Color.BLACK) for i in range(len(Board.LETTERS))]

        for i in range(len(Board.LETTERS) - 4):
            b[i+2] = [Empty() for i in range(len(Board.LETTERS))]

        b[6] = [Pawn(Color.WHITE) for i in range(len(Board.LETTERS))]
        b[7] = [Rook(Color.WHITE), Knight(Color.WHITE), \
             Bishop(Color.WHITE), Queen(Color.WHITE), King(Color.WHITE), \
                 Bishop(Color.WHITE), Knight(Color.WHITE), Rook(Color.WHITE)]  
        return b

    def __str__(self):

        board_str = "\n       "

        for c in Board.LETTERS:
            board_str += " {0}  ".format(c)
        
        board_str += "\n       "

        for c in range(len(Board.LETTERS)):
            board_str += "--- "

        board_str += "\n   "

        for i, n in enumerate(Board.NUMBERS):
            board_str += " {0} | ".format(n)

            for piece in self.board[i]:
                board_str += "{0} | ".format(piece.__str__())

            board_str += "\n       "

            for c in Board.LETTERS:
                board_str += "--- "

            board_str += "\n   "
        
        return board_str

    def get_board(self):
        return self.board

    def get_position(self):
        pass