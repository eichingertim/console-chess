from .base_piece import BasePiece
from .piece_type import PieceType
from .empty import Empty
from .color import Color

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

        # Checks if it's a diagonal movement
        if (cur_col, cur_row) != (dest_row, dest_col) or \
             abs(cur_col - dest_col) != abs(cur_row - dest_row):
            return False

        direction = (1 if cur_row - dest_row < 0 else - 1, \
            1 if cur_col - dest_col < 0 else -1)

        # Determine which direction to check
        return self.check_move_for_direction(direction, \
                (dest_row, dest_col), (cur_row, cur_col), board)
        

    def check_move_for_direction(self, dir, destPos, curPos, board):
        for distance in range(1, 8):
            move = (distance * dir[0], distance*dir[1])
            new_pos = (curPos[0] + move[0], curPos[1] + move[1])

            if board.is_valid_pos(new_pos):
                piece_at_pos = board.board[new_pos[0]][new_pos[1]]

                if isinstance(piece_at_pos, Empty):
                    if (new_pos == destPos):
                        return True
                else:
                    if piece_at_pos.color == self.color:
                        return False
                    else:
                        if (new_pos == destPos):
                            return True
                        else:
                            return False
            else:
                return False
        
        return False

    

        
