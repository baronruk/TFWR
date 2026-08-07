from constants import HAY_ROWS, PUMPKIN_COLUMNS, VEGETABLE_ROWS, WOOD_ROWS, WORLD_SIZE
from helpers import cultivate, do_harvest, hydrate
from utilities import is_even


def farm_mixed():
    for i in range(WORLD_SIZE):
        current_row = get_pos_y()
        current_column = get_pos_x()

        # carrots/pumkings
        if current_row in VEGETABLE_ROWS:
            do_harvest()
            cultivate()
            if current_column in PUMPKIN_COLUMNS:
                hydrate(0.5)
                plant(Entities.Pumpkin)
            else:
                plant(Entities.Carrot)

        # hay
        if current_row in HAY_ROWS:
            do_harvest()
            plant(Entities.Grass)

        # wood
        if current_row in WOOD_ROWS:
            do_harvest()

            if is_even(get_pos_x()):
                plant(Entities.Bush)
            else:
                # hydrate(0.75)
                plant(Entities.Tree)

        if current_row == (WORLD_SIZE - 1):
            move(East)

        move(North)
