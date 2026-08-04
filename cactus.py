from constants import WORLD_SIZE
from helpers import get_coords, reverse


def plant_cactus():
    if get_ground_type() == Grounds.Grassland:
        till()
    plant(Entities.Cactus)


def farm_cactus():
    direction = North
    vertical_direction = East
    horizontal_sorted = False
    vertical_sorted = False

    # planting
    for column in range(WORLD_SIZE):
        for row in range(WORLD_SIZE):
            plant_cactus()

            if row != WORLD_SIZE - 1:
                move(direction)

        if column != WORLD_SIZE - 1:
            move(vertical_direction)

        direction = reverse(direction)
    vertical_direction = reverse(vertical_direction)

    # sorting
    while not horizontal_sorted or not vertical_sorted:
        horizontal_sorted = True
        vertical_sorted = True

        for i in range(WORLD_SIZE):
            for j in range(WORLD_SIZE):
                x, y = get_coords()

                current_cactus = measure()
                north_cactus = measure(North)
                south_cactus = measure(South)
                west_cactus = measure(West)
                east_cactus = measure(East)

                # sort north/south
                if (
                    y != WORLD_SIZE - 1
                    and north_cactus != None
                    and direction == North
                    and current_cactus > north_cactus
                ):
                    swap(North)
                    horizontal_sorted = False

                if (
                    y != 0
                    and south_cactus != None
                    and direction == South
                    and current_cactus < south_cactus
                ):
                    swap(South)
                    horizontal_sorted = False

                # sort east/west
                if x != 0 and west_cactus != None and current_cactus < west_cactus:
                    swap(West)
                    vertical_sorted = False

                if x != WORLD_SIZE - 1 and east_cactus != None and current_cactus > east_cactus:
                    swap(East)
                    vertical_sorted = False

                if direction == North:
                    if y != WORLD_SIZE - 1:
                        move(North)
                else:
                    if y != 0:
                        move(South)

            if vertical_direction == East:
                if x != WORLD_SIZE - 1:
                    move(East)
            else:
                if x != 0:
                    move(West)

            direction = reverse(direction)
        vertical_direction = reverse(vertical_direction)

    # harvesting
    harvest()
