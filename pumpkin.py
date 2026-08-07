from constants import WORLD_GRID_AREA, WORLD_SIZE
from helpers import cultivate, do_harvest, hydrate, reverse


def plant_healthy_pumpkin():
    cultivate()

    # measure
    # returns a mysterious number Entities.Pumpkin
    # returns None for Entities.Dead_Pumpkin
    while measure() == None:
        hydrate(1, True)
        plant(Entities.Pumpkin)

        # sleep
        do_a_flip()


def farm_pumpkin():
    healthy_pumpkins = 0
    direction = East
    vertical_direction = North

    while True:
        for column in range(WORLD_SIZE):
            for row in range(WORLD_SIZE):
                plant_healthy_pumpkin()

                if get_entity_type() == Entities.Pumpkin:
                    healthy_pumpkins += 1

                if healthy_pumpkins == WORLD_GRID_AREA:
                    do_harvest()
                    healthy_pumpkins = 0

                if row != WORLD_SIZE - 1:
                    move(vertical_direction)

            if column != WORLD_SIZE - 1:
                move(direction)

            vertical_direction = reverse(vertical_direction)
        direction = reverse(direction)
