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
    NUMBERS = [i for i in range(1, 9)].reverse()

    def __init__(self):
        self.board = [8][8]
        self.create_board()

    def create_board(self):
        self.create_black_pieces
        self.create_white_pieces

    def create_black_pieces(self):
        board[0][0] = Rook(Color.BLACK);
        board[0][1] = Knight(Color.BLACK);
        board[0][2] = Bishop(Color.BLACK);
        board[0][3] = Queen(Color.BLACK);
        board[0][4] = King(Color.BLACK);
        board[0][5] = Bishop(Color.BLACK);
        board[0][6] = Knight(Color.BLACK);
        board[0][7] = Rook(Color.BLACK);

        for i in range(0, 8):
            board[1][i] = Pawn(Color.BLACK);

    def create_white_pieces(self):
        board[7][0] = Rook(Color.WHITE);
        board[7][1] = Knight(Color.WHITE);
        board[7][2] = Bishop(Color.WHITE);
        board[7][3] = Queen(Color.WHITE);
        board[7][4] = King(Color.WHITE);
        board[7][5] = Bishop(Color.WHITE);
        board[7][6] = Knight(Color.WHITE);
        board[7][7] = Rook(Color.WHITE);

        for i in range(0, 8):
            board[6][i] = Pawn(Color.BLACK);

    def __str__(self):
        # TODO: string representation