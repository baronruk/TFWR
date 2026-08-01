from helpers import do_haverst, hydrate
from utilities import is_even

ROWS = {
    'first': 0,
    'second': 1,
    'third': 2,
    'fourth': 3,
    'fifth': 4,
    'sixth': 5,
    'seventh': 6,
    'eighth': 7,
}
VEGETABLE_ROWS = [
    ROWS['first'],
    ROWS['second'],
    ROWS['seventh'],
    ROWS['eighth'],
]
PUMPKIN_COLUMNS = [
    0,
    1,
    4,
    5,
]
WORLD_SIZE = get_world_size()

while True:
    # pet_the_piggy()

    for i in range(WORLD_SIZE):
        current_row = get_pos_y()
        current_column = get_pos_x()

        # carrots/pumkings
        if current_row in VEGETABLE_ROWS:
            do_haverst()
            if get_ground_type() == Grounds.Grassland:
                till()
            if current_column in PUMPKIN_COLUMNS:
                hydrate(0.5)
                plant(Entities.Pumpkin)
            else:
                plant(Entities.Carrot)

        # hay
        if (current_row == ROWS['third']) or (current_row == ROWS['fourth']):
            do_haverst()
            plant(Entities.Grass)

        # wood
        if (current_row == ROWS['fifth']) or (current_row == ROWS['sixth']):
            do_haverst()

            if is_even(get_pos_x()):
                plant(Entities.Bush)
            else:
                hydrate(0.75)
                plant(Entities.Tree)

        if current_row == (WORLD_SIZE - 1):
            move(East)

        move(North)
