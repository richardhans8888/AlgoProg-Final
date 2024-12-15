import pygame, sys
from game import Game
from colors import Colors

pygame.init()

# Fonts and text for the game interface.
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Rectangles for "Score" and "Next Block" display areas.
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Screen setup and game initialization.
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()
game = Game()

# Custom event for game updates (e.g., moving blocks down every 200ms).
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Main game loop.
while True:
    for event in pygame.event.get():
        # Quit the game.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle keyboard inputs.
        if event.type == pygame.KEYDOWN:
            if game.game_over:  # Restart game if over.
                game.game_over = False
                game.reset()
            elif event.key == pygame.K_LEFT and not game.game_over:  # Move block left.
                game.move_left()
            elif event.key == pygame.K_RIGHT and not game.game_over:  # Move block right.
                game.move_right()
            elif event.key == pygame.K_DOWN and not game.game_over:  # Move block down faster.
                game.move_down()
                game.update_score(0, 1)
            elif event.key == pygame.K_UP and not game.game_over:  # Rotate block.
                game.rotate()

        # Automatically move block down at intervals.
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Drawing the game interface.
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.fill(Colors.dark_blue)  # Background color.
    screen.blit(score_surface, (365, 20))  # Display "Score" text.
    screen.blit(next_surface, (375, 180))  # Display "Next" text.

    # Display "GAME OVER" text if the game is over.
    if game.game_over:
        screen.blit(game_over_surface, (320, 450))

    # Draw rectangles for "Score" and "Next Block".
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, 
                                                                  centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    # Draw the game grid and current block.
    game.draw(screen)

    # Update the screen and control the frame rate.
    pygame.display.update()
    clock.tick(60)