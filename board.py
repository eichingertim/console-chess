from pieces.base_piece import BasePiece
from pieces.color import Color
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.pawn import Pawn
from pieces.king import King

class Board:

    LETTERS = [chr(i) for i in range(65, 73)]
    NUMBERS = [i for i in range(1, 9)]
    NUMBERS.reverse()

    print(NUMBERS)

    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        self.create_black_pieces()
        self.create_white_pieces()

    def create_black_pieces(self):
        self.board[0][0] = Rook(Color.BLACK)
        self.board[0][1] = Knight(Color.BLACK)
        self.board[0][2] = Bishop(Color.BLACK)
        self.board[0][3] = Queen(Color.BLACK)
        self.board[0][4] = King(Color.BLACK)
        self.board[0][5] = Bishop(Color.BLACK)
        self.board[0][6] = Knight(Color.BLACK)
        self.board[0][7] = Rook(Color.BLACK)

        print(self.board)

        for i in range(0, 8):
            self.board[1][i] = Pawn(Color.BLACK)

    def create_white_pieces(self):
        self.board[7][0] = Rook(Color.WHITE)
        self.board[7][1] = Knight(Color.WHITE)
        self.board[7][2] = Bishop(Color.WHITE)
        self.board[7][3] = Queen(Color.WHITE)
        self.board[7][4] = King(Color.WHITE)
        self.board[7][5] = Bishop(Color.WHITE)
        self.board[7][6] = Knight(Color.WHITE)
        self.board[7][7] = Rook(Color.WHITE)

        for i in range(0, 8):
            self.board[6][i] = Pawn(Color.BLACK)

    def __str__(self):
        # TODO: string representation

        board_str = "\n   "

        for c in Board.LETTERS:
            board_str += "  \u202F\u202F{0}\u202F".format(c)
        
        board_str += "\n   "

        for c in Board.LETTERS:
            board_str += "-----"

        board_str += "\n   "

        for i, n in enumerate(Board.NUMBERS):
            board_str += " {0} | ".format(n)

            print(self.board)

            for piece in self.board[i]:
                if (piece):
                    board_str += "{0} | ".format(piece.__str__())
                else:
                    board_str += "\u26DA | "

            board_str += "\n   "

            for c in Board.LETTERS:
                board_str += "-----"

            board_str += "\n   "
        
        return board_str
