def do_haverst():
    if can_harvest():
        harvest()


def hydrate(threshold):
    water_level = get_water()

    if water_level < threshold:
        use_item(Items.Water)
