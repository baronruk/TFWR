from constants import WORLD_SIZE
from helpers import cultivate, do_harvest, reverse


def plant_grass():
    cultivate()
    plant(Entities.Grass)


def haverst_grass():
    if get_entity_type() == Entities.Grass:
        do_harvest()


def farm_hay():
    direction = East
    vertical_direction = North

    while True:
        for column in range(WORLD_SIZE):
            for row in range(WORLD_SIZE):
                haverst_grass()
                plant_grass()

                if row != WORLD_SIZE - 1:
                    move(vertical_direction)

            if column != WORLD_SIZE - 1:
                move(direction)

            vertical_direction = reverse(vertical_direction)
        direction = reverse(direction)

        # sleep
        do_a_flip()
