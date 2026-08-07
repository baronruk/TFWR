def cultivate():
    if get_ground_type() == Grounds.Grassland:
        till()


def do_harvest():
    if can_harvest():
        harvest()


def get_coords():
    return get_pos_x(), get_pos_y()


def hydrate(threshold, force=False):
    if force:
        while get_water() < threshold:
            use_item(Items.Water)
    else:
        water_level = get_water()

        if water_level < threshold:
            use_item(Items.Water)


def reset_position():
    x, y = get_coords()
    while x != 0 or y != 0:
        if x != 0:
            move(West)
        if y != 0:
            move(South)
        x, y = get_coords()


def reverse(direction):
    if direction == West:
        return East
    if direction == East:
        return West
    if direction == North:
        return South
    if direction == South:
        return North
