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
        self.black_king = King(Color.BLACK)
        self.white_king = King(Color.WHITE)
        self.board = self.create_board()
        self.is_game_over = False

    def create_board(self):
        b = np.zeros((8,8), dtype=BasePiece)
        b[0] = [Rook(Color.BLACK), Knight(Color.BLACK), \
             Bishop(Color.BLACK), Queen(Color.BLACK), self.black_king, \
                 Bishop(Color.BLACK), Knight(Color.BLACK), Rook(Color.BLACK)]
        b[1] = [Pawn(Color.BLACK) for i in range(len(Board.LETTERS))]

        for i in range(len(Board.LETTERS) - 4):
            b[i+2] = [Empty() for i in range(len(Board.LETTERS))]

        b[6] = [Pawn(Color.WHITE) for i in range(len(Board.LETTERS))]
        b[7] = [Rook(Color.WHITE), Knight(Color.WHITE), \
             Bishop(Color.WHITE), Queen(Color.WHITE), self.white_king, \
                 Bishop(Color.WHITE), Knight(Color.WHITE), Rook(Color.WHITE)]  
        return b

    def move(self, start_pos, end_pos):
        # Special turn en passant
        if not self.check_en_passant(start_pos, end_pos):
            # Normal turn
            self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = Empty()

        # Special turn rochade
        self.check_rochade(start_pos, end_pos)

    def check_en_passant(self, start_pos, end_pos):
        if self.board[start_pos[0]][start_pos[1]].piece_type == PieceType.PAWN and abs(start_pos[1] - end_pos[1] == 1):
            if isinstance(self.board[end_pos[0]][end_pos[1]], Empty):
                # removes the enemy pawn
                self.board[start_pos[0]][end_pos[1]] = Empty()
                return True
        return False

    def check_rochade(self, start_pos, end_pos):
        if self.board[end_pos[0]][end_pos[1]].piece_type == PieceType.KING or self.board[end_pos[0]][end_pos[1]].piece_type == PieceType.ROOK:
            self.board[end_pos[0]][end_pos[1]].is_moved = True
            if self.board[end_pos[0]][end_pos[1]].piece_type == PieceType.KING and abs(start_pos[1] - end_pos[1]) >= 0:
                # moves rook
                direction = -1 if end_pos[1] - start_pos[1] < 0 else 1
                rook = self.board[end_pos[0]][end_pos[1]+direction]
                self.board[end_pos[0]][end_pos[1] - direction] = rook
                self.board[end_pos[0]][end_pos[1] + direction] = Empty()
                self.board[end_pos[0]][end_pos[1] - direction].is_moved = True

    def check_for_check(self, last_move_color):
        king_pos = self.get_king_pos(Color.BLACK if last_move_color == Color.WHITE else Color.WHITE)

        for row in self.board:
            for piece in row:
                if piece.color == last_move_color and piece.can_move(self, king_pos[0], king_pos[1]):
                    return True
        
        return False

    def check_for_check_mate(self, last_moved_color):

        b = copy.deepcopy(self)
        moves = list()

        # 1.) go thorugh all possible pieces !last_moved_color
        for row in b.get_board():
            for piece in row:
                # 2.) get all possible moves

                if (piece.color != last_moved_color):
                    for i in range(len(b.get_board())):
                        for j in range(len(b.get_board()[0])):
                            if piece.can_move(b, i, j):
                                moves.append((b.get_position(piece), (i,j)))
                else:
                    continue

                 # 3.) make that moves
                for m in moves:
                    b_copy = copy.deepcopy(b)
                    b_copy.move(m[0], m[1])

                    king_pos = b_copy.get_king_pos(Color.BLACK if last_moved_color == Color.WHITE else Color.WHITE)

                    can_attack = False
                    # 4.) check for last_moved_color all pieces, if it can attack king
                    for r in b_copy.get_board():
                        for p in r:
                            if p.color == last_moved_color and p.can_move(b_copy, king_pos[0], king_pos[1]):
                                can_attack = True
                    
                    if not can_attack:
                        return False
        
        return True



                            

               
                
                

    def get_king_pos(self, color):
        for r in self.board:
            for p in r:
                if p.color == color and p.piece_type == PieceType.KING:
                    return self.get_position(p)

        return None

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