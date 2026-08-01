FIRST_ROW = 0
SECOND_ROW = 1
THIRD_ROW = 2
FOURTH_ROW = 3
FIFTH_ROW = 4
SIXTH_ROW = 5
SEVENTH_ROW = 6
EIGHTH_ROW = 7
VEGETABLE_ROWS = [
    FIRST_ROW,
    SECOND_ROW,
    SEVENTH_ROW,
    EIGHTH_ROW,
]
PUMPKIN_COLUMNS = [
    0,
    1,
    4,
    5,
]
WORLD_SIZE = get_world_size()


def do_haverst():
    if can_harvest():
        harvest()


def hydrate(threshold):
    water_level = get_water()

    if water_level < threshold:
        use_item(Items.Water)


def is_even(number):
    return number % 2 == 0


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
        if (current_row == THIRD_ROW) or (current_row == FOURTH_ROW):
            do_haverst()
            plant(Entities.Grass)

        # wood
        if (current_row == FIFTH_ROW) or (current_row == SIXTH_ROW):
            do_haverst()

            if is_even(get_pos_x()):
                plant(Entities.Bush)
            else:
                hydrate(0.75)
                plant(Entities.Tree)

        if current_row == (WORLD_SIZE - 1):
            move(East)

        move(North)
