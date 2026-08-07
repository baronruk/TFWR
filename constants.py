ROWS = {
    'first': 0,
    'second': 1,
    'third': 2,
    'fourth': 3,
    'fifth': 4,
    'sixth': 5,
    'seventh': 6,
    'eighth': 7,
    'ninth': 8,
    'tenth': 9,
    'eleventh': 10,
    'twelfth': 11,
    'thirteenth': 12,
    'fourteenth': 13,
    'fifteenth': 14,
    'sixteenth': 15,
}
HAY_ROWS = [
    ROWS['third'],
    ROWS['fourth'],
    ROWS['ninth'],
    ROWS['tenth'],
    ROWS['fifteenth'],
    ROWS['sixteenth'],
]
VEGETABLE_ROWS = [
    ROWS['first'],
    ROWS['second'],
    ROWS['seventh'],
    ROWS['eighth'],
    ROWS['thirteenth'],
    ROWS['fourteenth'],
]
WOOD_ROWS = [
    ROWS['fifth'],
    ROWS['sixth'],
    ROWS['eleventh'],
    ROWS['twelfth'],
]
PUMPKIN_COLUMNS = [
    0,
    1,
    4,
    5,
    8,
    9,
    12,
    13,
]
WORLD_SIZE = get_world_size()
WORLD_GRID_AREA = WORLD_SIZE * WORLD_SIZE
