from constants import WORLD_SIZE
from helpers import cultivate, do_harvest, reset_position, reverse


def plant_carrot():
    cultivate()
    plant(Entities.Carrot)


def haverst_carrot():
    if get_entity_type() == Entities.Carrot:
        do_harvest()


def farm_carrot():
    while True:
        direction = East
        vertical_direction = North

        for column in range(WORLD_SIZE):
            for row in range(WORLD_SIZE):
                haverst_carrot()
                plant_carrot()

                if row != WORLD_SIZE - 1:
                    move(vertical_direction)

            if column != WORLD_SIZE - 1:
                move(direction)

            vertical_direction = reverse(vertical_direction)

        reset_position()
