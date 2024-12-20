import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Final Project")

LIGHT_PINK = (255, 182, 193)
PASTEL_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)

# Load images
sprite_left = pygame.image.load("images/CharaSideL.png")
sprite_right = pygame.image.load("images/CharaSideR.png")
sprite_forward = pygame.image.load("images/CharaFront.png")
background_object = pygame.image.load("images/buildings.png")

road_image = pygame.image.load("images/road.png")
road_rect = road_image.get_rect()
road_rect.topleft = (0, HEIGHT - 100)  

background_object = pygame.transform.scale(background_object, (WIDTH, HEIGHT))

sprite_rect = sprite_forward.get_rect()  
sprite_rect.centerx = WIDTH // 2  
sprite_rect.bottom = road_rect.top  

velocity = 5  

class Sparkle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.alpha = random.randint(100, 255)  
        self.alpha_direction = random.choice([-1, 1])  
        self.max_alpha = 255
        self.min_alpha = 50

    def update(self):
        if self.alpha_direction == 1:
            self.alpha += 2
            if self.alpha >= self.max_alpha:
                self.alpha = self.max_alpha
                self.alpha_direction = -1  
        else:
            self.alpha -= 2
            if self.alpha <= self.min_alpha:
                self.alpha = self.min_alpha
                self.alpha_direction = 1  

    def draw(self, surface):
        sparkle_color = (255, 255, 255)
        sparkle_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)  
        pygame.draw.polygon(sparkle_surface, sparkle_color, [
            (self.size, 0), (self.size * 2, self.size), (self.size, self.size * 2), (0, self.size)
        ])
        sparkle_surface.set_alpha(self.alpha)
        surface.blit(sparkle_surface, (self.x - self.size, self.y - self.size))

def create_gradient():
    for y in range(HEIGHT):
        color = [
            LIGHT_PINK[0] + (PASTEL_BLUE[0] - LIGHT_PINK[0]) * y // HEIGHT,
            LIGHT_PINK[1] + (PASTEL_BLUE[1] - LIGHT_PINK[1]) * y // HEIGHT,
            LIGHT_PINK[2] + (PASTEL_BLUE[2] - LIGHT_PINK[2]) * y // HEIGHT
        ]
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

# Main game loop
running = True
current_sprite = sprite_forward  

sparkles = []
sparkle_timer = 0

while running:
    screen.fill((0, 0, 0))
    create_gradient()
    
    screen.blit(background_object, (0, 0))
    screen.blit(road_image, road_rect)

    for sparkle in sparkles:
        sparkle.update()
        sparkle.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input for movement
    keys = pygame.key.get_pressed()
    
    # Horizontal movement (left and right) with platform constraints
    if keys[pygame.K_LEFT]:
        if sprite_rect.left > road_rect.left:  # Ensure character doesn't go off the left side of the road
            sprite_rect.x -= velocity
        current_sprite = sprite_left  # Show the left-facing sprite
    elif keys[pygame.K_RIGHT]:
        if sprite_rect.right < road_rect.right:  # Ensure character doesn't go off the right side of the road
            sprite_rect.x += velocity
        current_sprite = sprite_right  # Show the right-facing sprite

    # Vertical movement (up-down) constrained to the platform
    if keys[pygame.K_UP]:
        if sprite_rect.top > road_rect.top:  # Prevent moving above the platform
            sprite_rect.y -= velocity
        current_sprite = sprite_forward  # Keep the forward-facing sprite
    elif keys[pygame.K_DOWN]:
        if sprite_rect.bottom < road_rect.bottom:  # Prevent moving below the platform
            sprite_rect.y += velocity
        current_sprite = sprite_forward  # Keep the forward-facing sprite

    # Constrain the character's vertical position to the platform's y-coordinate
    if sprite_rect.bottom > road_rect.top:
        sprite_rect.bottom = road_rect.top  # Place character on the platform


    # Draw the character sprite
    screen.blit(current_sprite, sprite_rect)

    sparkle_timer += 1
    if sparkle_timer >= 15:
        sparkle_timer = 0
        new_sparkle = Sparkle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(2, 5))
        sparkles.append(new_sparkle)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
