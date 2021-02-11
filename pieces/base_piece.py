class BasePiece:

    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

    def can_move(self, board, dest_row, dest_col):
        pass

    def __eq__(self, piece):
        return piece is self

    def __str__(self):
        pass

    def get_color(self):
        return self.color