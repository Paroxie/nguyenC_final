import pygame 
import random


pygame.init()


# Display (test background)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Final Project")

Pink = (255, 182, 193)
Blue = (173, 216, 230)
White = (255, 255, 255)

sprite_left = pygame.image.load("CharaSideL.png")
sprite_right = pygame.image.load("CharaSideR.png")
sprite_forward = pygame.image.load("CharaFront.png")

background_object = pygame.image.load("object_test.png")  

sprite_rect = sprite_forward.get_rect()  
sprite_rect.center = (WIDTH // 2, HEIGHT // 2)  

velocity = 5  #

class sparkles:
    def __init__(self, x, y, size): 
        self.x = x
        self.y = y
        self.size = size
        self.alpha = random.randint(100, 255)  #
        self.alpha_direction = random.choice([-1, 1])  # Fade in or out
        self.max_alpha = 255
        self.min_alpha = 50

    def update(self):
        if self.alpha_direction == 1:
            self.alpha += 2
            if self.alpha >= self.max_alpha:
                self.alpha = self.max_alpha
                self.alpha_direction = -1
        else:
            self.alpha -+ 2
            if self.alpha <= self.min_alpha:
                self.alpha = self.min_alpha
                self.alpha_direction = 1
    
    def draw(self, surface):
        sparkle_color = (White[0], White[1], White[2], self.alpha)
        diamond = [
            (self.x, self.y - self.size),  
            (self.x + self.size, self.y),  
            (self.x, self.y + self.size),  
            (self.x - self.size, self.y)
        ]
        pygame.draw.polygon(surface, sparkle_color, diamond)


def create_gradient():
    for y in range(HEIGHT):
        color = [
            Pink[0] + (Blue[0] - Pink[0]) * y // HEIGHT,
            Pink[1] + (Blue[1] - Pink[1]) * y // HEIGHT,
            Pink[2] + (Blue[2] - Pink[2]) * y // HEIGHT
        ]
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

running = True
current_sprite = sprite_forward #default 

sparkles = []

sparkle_timer = 0

while running: 
    screen.fill((0, 0, 0))
    create_gradient()

    screen.blit(background_object, (0, 0))

    for event in pygame.evemt.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sprite_rect.x -= velocity
        current_sprite = sprite_left  # Show the left-facing sprite
    elif keys[pygame.K_RIGHT]:
        sprite_rect.x += velocity
        current_sprite = sprite_right  # Show the right-facing sprite
    elif keys[pygame.K_UP]:
        sprite_rect.y -= velocity
        current_sprite = sprite_forward  # Keep the forward-facing sprite
    elif keys[pygame.K_DOWN]:
        sprite_rect.y += velocity
        current_sprite = sprite_forward  # Keep the forward-facing sprite

    screen.blit(current_sprite, sprite_rect)

    sparkle_timer += 1
    if sparkle_timer >= 15:
        sparkle_timer = 0
        new_sparkle = Sparkle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(2, 5))
        sparkle.append(new_sparkle)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()