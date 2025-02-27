import pygame
from pygame import Vector2
from random import randint

pygame.init()

import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the path to the image relative to the script directory
bird_wing_up_path = os.path.join(script_dir, "images", "bird_wing_up.png")

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

dt = 0 # delta time = infinitsmall change in time
vy = 0
ball_pos = Vector2(screen.get_width()/10, screen.get_height()/2)
g = 9.81 # freefall acceleration on earth 
spawn_time = 0

class Bird(pygame.sprite.Sprite):
    """
    Bird Class

    Attributes:
    - ball_pos: Creates a vector object with the initial position of the bird at the left of the screen
    - radius: radius of the bird
    - vy: vertical velocity of the bird
    - image: image of the bird
    - rect: rectangle object with the initial position of the bird and dimensions set
    - rect.x: x position of the bird
    - rect.y: y position of the bird

    Behaviors:
    - __init__(): creates the bird
    - __repr__(): returns a string representation of the bird
    - update(): updates the position of the bird. physics calculations. 
    -> when space is pressed, the bird jumps, and if the absolute downwards velocity is high enough, then it can keep increasing the velocity

    """

    def __init__(self):
        super().__init__()
        self.ball_pos = Vector2(screen.get_width()/10, screen.get_height()/2)
        self.radius = 40
        self.vy = 0
        self.image = pygame.image.load(bird_wing_up_path).convert_alpha()
        self.rect = self.image.get_rect(center=self.ball_pos)
        self.rect.x = self.ball_pos.x
        self.rect.y = self.ball_pos.y
        self.keys = None

    def __repr__(self):
        return f"{super().__repr__()}"
    
    def update(self):
        global dt
        global g
        
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_SPACE]:
            self.vy = -110
            if self.vy<-90:
                self.vy += self.vy          

        if self.vy > 0:
            self.accy = g*60
        else:
            self.accy = g*45
        # physics calculations
        self.vy += self.accy*dt # POSITIVE DIRECTION IS DOWNWARDS
        self.ball_pos.y += self.vy*dt

        self.rect.x = self.ball_pos.x
        self.rect.y = self.ball_pos.y

class Barrier(pygame.sprite.Sprite):
    """
    Barrier Class

    Attributes:
    - barr_pos: Creates a vector object with the initial position of the barrier at the right of the screen
    - rect: rectangle object with the initial position of the barrier and dimensions set
    - rect.x: x position of the barrier
    - rect.y: y position of the barrier
    - passed: bool
    - type: 0 for normal/green barrier, 1 for double-pointer/golden barrier

    Behaviors:
    - __init__(type): creates the barrier. recieves the type of barrier, 0 for normal/green barrier, 1 for double-pointer/golden barrier
    - update(): updates the position of the barrier
    - draw(screen): draws the barrier on the screen

    """

    pair = 0 # barriers are created in pairs

    def __init__(self, type):
        super().__init__()
        self.barr_pos = Vector2(screen.get_width()*1.1)
        self.rect = pygame.Rect(self.barr_pos.x, self.barr_pos.y, 50, 300)
        self.rect.x = self.barr_pos.x
        self.rect.y = self.barr_pos.y
        self.passed = False
        self.type = type
        print(f"Type: {self.type}") # for debugging

        if Barrier.pair % 2 == 0: # creates the top barrier
            self.rect.y = screen.get_height()*(-(randint(1,3)/10))
        else: # creates the bottom barrier, and ensures the gap is not too small by checking the position of the top barrier in the pair
            if list(barriers)[len(barriers)-1].rect.y > screen.get_height()*((-2)/10) and Barrier.pair > 0:
                self.rect.y = screen.get_height()*(randint(7,10)/10)
                print("Way too high avoided")
            else: 
                self.rect.y = screen.get_height()*(randint(5,9)/10)

        Barrier.pair += 1
        print(Barrier.pair)
        print(Barrier.__repr__(self))
        
    def __repr__(self):
        return (f"Barrier({self.rect.x}, {self.rect.y})")

    def update(self):
        
        self.rect.x -= 5
        if self.rect.x < -50:
            self.kill()
            del self
            print("deleted")

    
    def draw(self, screen):
        if self.type == 0:
            pygame.draw.rect(screen, "green", self.rect)
        elif self.type == 1:
            pygame.draw.rect(screen, (255, 215, 0), self.rect)

def check_collision(sprite1, sprite2):
    rect1 = sprite1.rect
    rect2 = sprite2.rect
    overlap = rect1.clip(rect2)
    if overlap.width == 0 or overlap.height == 0:
        return False
    for x in range(overlap.left, overlap.right):
        for y in range(overlap.top, overlap.bottom):
            sprite1_pixel = screen.get_at((x - rect1.x, y - rect1.y))
            sprite2_pixel = screen.get_at((x - rect2.x, y - rect2.y))
            if sprite1_pixel[3] > 0 and sprite2_pixel[3] > 0:
                return True
    return False

# Creates the a bird object 
bird = Bird()
bird_group = pygame.sprite.Group()
bird_group.add(bird)

barriers = pygame.sprite.Group() # basically a list of barriers
score = 0
real_score=0
game_over = False

font = pygame.font.Font(None, 36)
light_blue = (173, 216, 230)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fills the screen with light blue. This is done at the start so that it is behind everything making barriers and the bird seen
    screen.fill(light_blue)
    
    bird_group.update()
    bird_group.draw(screen)
    
    # Updates each barrier in the group. if a barrier collides with the bird, then the game is over
    for barrier in barriers:
        barrier.update()
        barrier.draw(screen)
        collided = check_collision(bird, barrier)
        if collided:
            game_over = True
            text = f"Game Over! Score: {score}"
            text_color = (0, 0, 0)  # White text
            text_surface = font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=(700, 100))  # Center of the screen
            pygame.display.flip()
            pygame.time.wait(3000) # Wait for 3 seconds
            running = False
            

    # Spawns barriers
    # Every 2 seconds, a barrier is spawned. It has a 30% chance of being a double-pointer/golden barrier
    spawn_time += dt
    if spawn_time > 2:
        chance = randint(0,10)/10
        if chance<0.3:
            barriers.add(Barrier(type=1)) # 1 for double-pointer/golden barrier
            barriers.add(Barrier(type=1))
        else:
            barriers.add(Barrier(type=0)) # 0 for normal/green barrier
            barriers.add(Barrier(type=0))
        print(f"Score is{real_score}")
        spawn_time = 0

    # Controls the scoring mechanism.
    # If the amount of frames that the bird contains a pixel further than the x position of a pixel in the barrier reaches 52, then the score is increased by 1
    for barrier in barriers:   
        if ball_pos.x>barrier.rect.x:
            barrier.passed = True
            if barrier.passed:
                score+=1
                delattr(barrier, 'passed')
                if score==52 and barrier.type==0:
                    real_score+=1
                    score=0
                    print(f"Score:{score}")
                    print(f"Real: {real_score}")
                elif score==52 and barrier.type==1:
                    real_score+=2
                    score=0
                    print(f"Score:{score}")
                    print(f"Real: {real_score}")
    
    # Displays the score
    # Done at the end so that it is on top of everything. High priority
    text = f"Score: {real_score}"
    text_color = (0, 0, 0)  # White text
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(700, 100))  # Center of the screen
    if score//52==0:
        screen.blit(text_surface, text_rect)

    # Updates the screen
    pygame.display.flip()

    # delta time, 60 frames per second
    dt = clock.tick(60)/10**3

pygame.quit()