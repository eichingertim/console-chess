from .base_piece import BasePiece
from .piece_type import PieceType
from .empty import Empty
from .color import Color
import operator

class Bishop(BasePiece):

    def __init__(self, color):
        super().__init__(PieceType.BISHOP, color)

    def __str__(self):
        if (self.color == Color.BLACK):
            return "\u265D"
        else:
            return "\u2657"

    def can_move(self, board, dest_row, dest_col):

        cur_row, cur_col = board.get_position(self) 

        # Checks if destination position is current position 
        # or it's not a diagonal movement
        if (cur_col, cur_row) == (dest_row, dest_col) or \
             abs(cur_col - dest_col) != abs(cur_row - dest_row):
            return False

        # calculates the direction we should check for the move
        direction = (1 if cur_row - dest_row < 0 else - 1, \
            1 if cur_col - dest_col < 0 else -1)

        # Determine which direction to check
        return self.check_move_for_direction(direction, \
                (dest_row, dest_col), (cur_row, cur_col), board)
        

    # goes through all fields in the given direction and checks if 
    # the piece can move to this point
    def check_move_for_direction(self, dir, destPos, curPos, board):
        for distance in range(1, 8):
            #TODO dir ist eigentlich schon vergeben?!
            move = (distance * dir[0], distance*dir[1])
            new_pos = tuple(map(operator.add, curPos, move))
            if board.is_valid_pos(new_pos):
                piece_at_pos = board.board[new_pos[0]][new_pos[1]]

                if isinstance(piece_at_pos, Empty):
                    if (new_pos == destPos):
                        return True
                else:
                    if piece_at_pos.color == self.color:
                        return False
                    else:
                        return new_pos == destPos
            else:
                return False
        
        return False

    

        
