import pygame
from sys import exit

from gameLogic import GameLogic
from sprites import get_game_tiles


pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)
game = GameLogic()
game.initialise_board()

tiles_group = pygame.sprite.Group()
tiles = get_game_tiles(screen.get_height(), screen.get_width(), game)

for tile in tiles:
    tiles_group.add(tile)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.capture_move_up()
            elif event.key == pygame.K_DOWN:
                game.capture_move_down()
            elif event.key == pygame.K_LEFT:
                game.capture_move_left()
            elif event.key == pygame.K_RIGHT:
                game.capture_move_right()

    tiles_group.update(game)
    tiles_group.draw(screen)
    pygame.display.flip()
    # this line ensures that the game runs at 60 fps max, we are doing this so that the game does not run too fast
    # the problem with running to fast would be that we would do the changes in pixel on each frame and the user would
    # not be able to see the changes or the changes will cause large effects on the game
    # for example if we move a player 1px each frame we would move 100px if the game runs at 100 fps,
    # and we will run 60px if the game runs at 60 fps
    clock.tick(60)
