import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

alien_width = 50
alien_height = 50
alien_speed = 3
alien_spawn_delay = 60

bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")
clock = pygame.time.Clock()

player_image = pygame.Surface((player_width, player_height))
player_image.fill(RED)

alien_image = pygame.Surface((alien_width, alien_height))
alien_image.fill(WHITE)

running = True
score = 0
alien_spawn_counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    if keys[pygame.K_SPACE]:
        bullet_x = player_x + player_width // 2 - bullet_width // 2
        bullet_y = player_y
        bullets.append((bullet_x, bullet_y))

    bullets = [(x, y - bullet_speed) for x, y in bullets]

    if alien_spawn_counter == 0:
        alien_x = random.randint(0, WIDTH - alien_width)
        alien_y = 0
        alien_spawn_counter = alien_spawn_delay
    else:
        alien_spawn_counter -= 1

    alien_y += alien_speed

    for bullet in bullets:
        if (
            alien_x < bullet[0] < alien_x + alien_width
            and alien_y < bullet[1] < alien_y + alien_height
        ):
            score += 1
            alien_y = 0
            alien_x = random.randint(0, WIDTH - alien_width)

    screen.fill(BLACK)
    screen.blit(player_image, (player_x, player_y))
    screen.blit(alien_image, (alien_x, alien_y))
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()