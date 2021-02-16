import re
import numpy as np
from board import Board
from .validation_model import ValidationModel

class Utils:

    WRONG_EXPRESSION = "Wrong expression! Try again"
    NOT_VALID_MOVE = "This move is not possible! Try again"
    WRONG_PIECES = "You cannot move with your enemie's piece! Try again"

    @staticmethod
    def is_valid_move(player, board, input):
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
        

    @staticmethod
    def is_valid_letter_number(input):
        if re.match(r"[A-H]", input[0]) and \
            re.match(r"[1-8]", input[1]):
            return True
        
        return False


    @staticmethod
    def is_valid_move_input(input):
        return len(input.split(" ")) == 3

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