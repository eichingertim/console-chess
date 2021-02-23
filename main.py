# ============================================================ #
# Abgabe Projektarbeit Einführung ins Programmieren mit Python
# Namen:
#     Tim Eichinger, Mat.Nr. 2089449
#     Timon Lorenz, Mat.Nr. 2101422

import sys
from game import Game

if __name__ == "__main__":

    major = sys.version_info.major
    minor = sys.version_info.minor

    if major == 3 and minor >= 8:
        Game().start_game()
    else:
        print("Please upgrade your python version to 3.8+")