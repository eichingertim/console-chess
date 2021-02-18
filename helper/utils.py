import re
import numpy as np
import copy
from board import Board
from pieces.color import Color
from .validation_model import ValidationModel

class Utils:

    WRONG_EXPRESSION = "Wrong expression! Try again"
    NOT_VALID_MOVE = "This move is not possible! Try again"
    WRONG_PIECES = "You cannot move with your enemie's piece! Try again"
    KING_NOT_SAVE = "This move is not possible! Your king would be checkmate"

    """
    Validates the entered move and checks if the king can be attacked.
    """
    @staticmethod
    def is_valid_move(player, board, input):
        
        if not (val := Utils.check_basic_movement(player, board, input)).b:
            return val

        start_pos, end_pos = val.start_pos, val.end_pos

        if Utils.king_can_be_attacked(board, player, start_pos, end_pos):
            return ValidationModel(False, None, None, Utils.KING_NOT_SAVE)
        
        return ValidationModel(True, start_pos, end_pos, None) 
    
    """
    Checks if the entered move is valid, without checking king attack
    """
    @staticmethod
    def check_basic_movement(player, board, input):
        if not Utils.is_valid_move_input(input):
            return ValidationModel(False, None, None, Utils.WRONG_EXPRESSION)

        input_str = input.split(" ")
        start_str, end_str = input_str[0], input_str[2]

        if not len(start_str) == len(end_str):
            return ValidationModel(False, None, None, Utils.WRONG_EXPRESSION)

        if not Utils.is_valid_letter_number(start_str) or \
            not Utils.is_valid_letter_number(end_str):
            return ValidationModel(False, None, None, Utils.WRONG_EXPRESSION)

        start_pos = Utils.convert_input_str_to_pos(start_str)
        end_pos = Utils.convert_input_str_to_pos(end_str)

        piece = board.get_board()[start_pos[0]][start_pos[1]]

        if not player.color == piece.color:
            return ValidationModel(False, None, None, Utils.WRONG_PIECES)

        if not piece.can_move(board, end_pos[0], end_pos[1]):
            return ValidationModel(False, None, None, Utils.NOT_VALID_MOVE)

        return ValidationModel(True, start_pos, end_pos, None)

    """
    Checks if the selected move would result in a checkmate
    """    
    @staticmethod
    def king_can_be_attacked(board, player, start_pos, end_pos):
        b = copy.deepcopy(board)
        b.move(start_pos, end_pos)
        if player.color == Color.WHITE:
            k_pos_r, k_pos_c = b.get_position(b.white_king)
            for row in b.get_board():
                for piece in row:
                    if piece.color == Color.BLACK and piece.can_move(b, k_pos_r, k_pos_c):
                        return True
        else:
            k_pos_r, k_pos_c = b.get_position(b.black_king)
            for row in b.get_board():
                for piece in row:
                    if piece.color == Color.WHITE and piece.can_move(b, k_pos_r, k_pos_c):
                        return True

        return False



    """
    Checks whether the entered move has valid numbers and letters
    """
    @staticmethod
    def is_valid_letter_number(input):
        if re.match(r"[A-H]", input[0]) and \
            re.match(r"[1-8]", input[1]):
            return True
        
        return False


    """
    checks if the entered move has a valid form: E6 to E7
    """
    @staticmethod
    def is_valid_move_input(input):
        return len(input.split(" ")) == 3

    """
    Converts a input position (e.g. E6) to the actual position in the 2D-Array
    """
    @staticmethod
    def convert_input_str_to_pos(input):

        pos = np.zeros(2, dtype=int)

        col, row = input

        for i in range(len(Board.LETTERS)):
            if Board.LETTERS[i] == col:
                print(Board.LETTERS[i])
                pos[1] = i
                break

        for i in range(len(Board.NUMBERS)-1, -1, -1):
            if Board.NUMBERS[i] == int(row):
                pos[0] = i
                break

        return pos