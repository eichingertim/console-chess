class BasePiece:

    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

    def __eq__(self, piece):
        if(not piece):
            return False 
        
        return piece.piece_type == self.piece_type and piece.color == self.color

    def __str__(self):
        pass

    def get_color(self):
        return self.color