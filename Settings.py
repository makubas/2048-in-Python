import numpy as np

EDGE_LENGTH = 400
CELL_COUNT = 4
CELL_PAD = 10

UP_KEY = "'w'"
DOWN_KEY = "'s'"
LEFT_KEY = "'a'"
RIGHT_KEY= "'d'"

LABEL_FONT = ("Verdana", 40, "bold")

GAME_COLOR = "#606060"
EMPTY_COLOR = "#808080"

POSSIBLE_MOVES_COUNT = 4
CELL_COUNT = 4
NUMBER_OF_SQUARES = CELL_COUNT * CELL_COUNT
NEW_TILE_DISTRIBUTION = np.array([2, 2, 2, 2, 2, 2, 2, 2 ,4, 4])

TILE_COLORS = {
    2: "#FF6666",
    4: "#FF5555", 
    8: "#FF4444", 
    16: "#FF3333",
    32: "#FF2222", 
    64: "#FF1111", 
    128: "#FF0000",
    256: "#DD0000", 
    512: "#BB0000", 
    1024: "#990000",
    2048: "#770000", 
    4096: "#550000", 
    8192: "#330000",
}

LABEL_COLORS = {
    2: "#011c08",
    4: "#011c08", 
    8: "#011c08", 
    16: "#011c08",
    32: "#011c08", 
    64: "#f2f2f0", 
    128: "#f2f2f0",
    256: "#f2f2f0", 
    512: "#f2f2f0", 
    1024: "#f2f2f0",
    2048: "#f2f2f0", 
    4096: "#f2f2f0", 
    8192: "#f2f2f0",
}