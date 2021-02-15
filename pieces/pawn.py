from .base_piece import BasePiece
from .piece_type import PieceType
from .empty import Empty
from .color import Color
import operator

class Pawn(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.PAWN, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265F"
        else:
            return "\u2659"
            
    #TODO Bauernumwandlung
    #TODO en passant

    def can_move(self, board, des_row, des_col):

        cur_row, cur_col =  board.get_position(self)

        # Checks if destination is current position
        if (cur_col, cur_row) == (des_row, des_col):
            return False

        # Checks if direction is allowed regarding their color
        if (self.color == Color.BLACK and des_row - cur_row > 0) or \
            (self.color == Color.WHITE and cur_row -des_row > 0):
            return False

        # Check normal move, double move and checks if he can beat
        if (des_col - cur_col == 0):
            # Check normal move
            if (abs(des_row - cur_row) == 1):
                move = (1 if self.color == Color.BLACK else -1, 0)
                new_pos = tuple(map(operator.add, (cur_row, cur_col), move))
                piece_at_pos = board.board[new_pos[0]][new_pos[1]]
                if isinstance(piece_at_pos, Empty):
                    return True
                else:
                    return False
            # Check double move
            else if (abs(des_row - cur_row) == 2):
                if(self.color == Color.BLACK):
                    return self.check_double_move(1, 1, (des_row, des_col), (cur_row, cur_col), board)
                else:
                    return self. check_double_move(6, -1, (des_row, des_col), (cur_row, cur_col), board)
            else: 
                return False
        else if (abs(des_col - cur_col) == 1):
            move = (1 if self.color == Color.BLACK else -1, (des_col - cur_col))
            new_pos = tuple(map(operator.add, (cur_row, cur_col), move))
            piece_at_pos = board.board[new_pos[0]][new_pos[1]]
            if isinstance(piece_at_pos, Empty):
                # beat en passant
                if (self.color == Color.BLACK):
                    return self.check_move_for_en_passant(4, (des_row, des_col), (cur_row, cur_col), board)
                else:
                    return self.check_move_for_en_passant(3, (des_row, des_col), (cur_row, cur_col), board)
            else:
                # beat normal
                if (piece_at_pos.color == self.color):
                    return False
                else:
                    return new_pos == (des_row, des_col)
        else:
            return False

    def check_double_move(self, start_row, direction, des_pos, cur_pos, board):
        if (cur_pos[0] == start_row):
            for i in range (1, 3):
                move = (i * direction, 0)
                new_pos = tuple(map(operator.add, cur_pos, move))
                piece_at_pos = board.board[new_pos[0]][new_pos[1]]

                if isinstance(piece_at_pos, Empty):
                    if(new_pos == des_pos):
                        return True
                else:
                    return False
        else:
            return False

    def check_move_for_en_passant(self, req_row, des_pos, cur_pos, board):
        pass