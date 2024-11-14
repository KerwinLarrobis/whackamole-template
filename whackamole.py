import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_rect = mole_image.get_rect(topleft=(0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        mole_rect.x = random.randrange(0, 608, 32)
                        mole_rect.y = random.randrange(0, 480, 32)
            screen.fill("light green")
            screen.blit(mole_image, mole_rect)
            for i in range(0, 20):
                pygame.draw.line(screen, "black", (32 * i, 0), (32 * i, 512))
                pygame.draw.line(screen, "black", (0, 32 * i), (640, 32 * i))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
# this is a comment