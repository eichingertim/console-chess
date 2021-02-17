from pieces.base_piece import BasePiece
from pieces.color import Color
from pieces.piece_type import PieceType
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.pawn import Pawn
from pieces.king import King
from pieces.empty import Empty
import numpy as np
import copy

class Board:

    LETTERS = [chr(i) for i in range(65, 73)]
    NUMBERS = [i for i in range(1, 9)]
    NUMBERS.reverse()

    def __init__(self):
        self.king_white = King(Color.WHITE)
        self.king_black = King(Color.BLACK)
        self.board = self.create_board()
        self.is_game_over = False

    def create_board(self):
        b = np.zeros((8,8), dtype=BasePiece)
        b[0] = [Rook(Color.BLACK), Knight(Color.BLACK), \
             Bishop(Color.BLACK), Queen(Color.BLACK), self.king_black, \
                 Bishop(Color.BLACK), Knight(Color.BLACK), Rook(Color.BLACK)]
        b[1] = [Pawn(Color.BLACK) for i in range(len(Board.LETTERS))]

        for i in range(len(Board.LETTERS) - 4):
            b[i+2] = [Empty() for i in range(len(Board.LETTERS))]

        b[6] = [Pawn(Color.WHITE) for i in range(len(Board.LETTERS))]
        b[7] = [Rook(Color.WHITE), Knight(Color.WHITE), \
             Bishop(Color.WHITE), Queen(Color.WHITE), self.king_white, \
                 Bishop(Color.WHITE), Knight(Color.WHITE), Rook(Color.WHITE)]  
        return b

    def move(self, start_pos, end_pos):
        piece = self.board[end_pos[0]][end_pos[1]]
        self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
        self.board[start_pos[0]][start_pos[1]] = Empty()

        # Set is moved for special turn rochade
        if self.board[end_pos[0]][end_pos[1]].piece_type == PieceType.KING:
            self.board[end_pos[0]][end_pos[1]].is_moved = True

        if piece.piece_type == PieceType.KING:
            self.is_game_over = True

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

    def get_position(self, piece):
        row, col = np.where(self.board == piece)
        return (row[0], col[0])

    def get_type(self, pos):
        return self.board[pos[0]][pos[1]].piece_type

    def set_piece(self, piece_type, color, pos):
        if(piece_type == "BISHOP"):
            self.board[pos[0]][pos[1]] = Bishop(color)
        elif(piece_type == "ROOK"):
            self.board[pos[0]][pos[1]] = Rook(color)
        elif(piece_type == "KNIGHT"):
            self.board[pos[0]][pos[1]] = Knight(color)
        else:
            self.board[pos[0]][pos[1]] = Queen(color)

    def is_valid_pos(self, pos):
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
            return True
        else:
            return False

    """
    def check_for_check_mate(self, color):

        k = self.king_white if color == Color.BLACK else self.king_black
        directions = [(1, 0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        can_move = [False, False, False, False, False, False, False, False]
        counter = 0

        for d in directions:
            board_copy = copy.deepcopy(self)
            b = board_copy.board
            rk, ck = self.get_position(k)
            try:
                if b[rk][ck].can_move(board_copy, rk+d[0], ck+d[1]):
                    b[rk+d[0]][ck+d[1]] = b[rk][ck]
                    b[rk][ck] = Empty()
                else:
                    can_move.remove(0)
                    continue
            except:
                can_move.remove(0)
                continue
            
            found = False
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if b[row][col].color != color:
                        if b[row][col].can_move(board_copy, rk+d[0], ck+d[1]):
                            can_move[counter] = True
                            break
                if found:
                    break
            
            counter += 1

        if len(can_move) == 0:
            return None

        c = color if all(ele == True for ele in can_move) else None

        print(can_move)

        if not c == None:
            self.is_game_over = True

        return c
"""