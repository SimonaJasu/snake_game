import pygame
from input_box import InputBox
from settings import *

def registration_screen(screen, font):
    input_box = InputBox(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 40, font)
    title = font.render("Enter your name:", True, (255, 255, 255))
    clock = pygame.time.Clock()
    done = False
    name = ""

    while not done:
        screen.fill((0, 0, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 2 - 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            input_box.handle_event(event)

        input_box.update()
        input_box.draw(screen)
        pygame.display.flip()

        if input_box.done and input_box.text.strip():
            name = input_box.text.strip()
            done = True
        clock.tick(30)

    return name