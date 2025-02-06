import pygame
from pygame import Vector2
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

dt = 0 # delta time = infinitsmall change in time
vy = 0
ball_pos = Vector2(screen.get_width()/10, screen.get_height()/2)
g = 9.81 # freefall acceleration on earth 
spawn_time = 0

class Barrier(pygame.sprite.Sprite):

    pair = 0

    def __init__(self):
        super().__init__()
        self.barr_pos = Vector2(screen.get_width()*1.1)
        self.rect = pygame.Rect(self.barr_pos.x, self.barr_pos.y, 50, 300)
        self.rect.x = self.barr_pos.x
        self.rect.y = self.barr_pos.y
        self.passed = False

        if Barrier.pair % 2 == 0:
            self.rect.y = screen.get_height()*(-(randint(1,3)/10))
        else:
            if list(barriers)[len(barriers)-1].rect.y > screen.get_height()*((-2)/10) and Barrier.pair > 0:
                self.rect.y = screen.get_height()*(randint(7,10)/10)
                print("Way too high avoided")
            else: 
                self.rect.y = screen.get_height()*(randint(5,9)/10)

        Barrier.pair += 1
        print(Barrier.pair)
        print(Barrier.__repr__(self))
        
    def __repr__(self):
        print(f"Barrier({self.rect.x}, {self.rect.y})")

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -50:
            self.kill()
            del self
            print("deleted")

    
    def draw(self, screen):
        pygame.draw.rect(screen, "green", self.rect)


barriers = pygame.sprite.Group() # basically a list of barriers

score = 0
real_score=0

font = pygame.font.Font(None, 36)

light_blue = (173, 216, 230)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fills the screen with light blue
    screen.fill(light_blue)

    # controlling the physics of the bird
    pygame.draw.circle(screen, "red", ball_pos, 40)

    for barrier in barriers:   
        if ball_pos.x>barrier.rect.x:
            barrier.passed = True
            if barrier.passed:
                score+=1
                delattr(barrier, 'passed')
                if score==52:
                    real_score+=1
                    score=0
                    print(f"Score:{score}")
                    print(f"Real: {real_score}")
    
    text = f"Score: {real_score}"
    text_color = (0, 0, 0)  # White text
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(700, 100))  # Center of the screen
    if score//52==0:
        screen.blit(text_surface, text_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        vy = -150
        if vy<-100:
            vy += vy/2
    

    for barrier in barriers:
        barrier.update()
        barrier.draw(screen)


    spawn_time += dt
    if spawn_time > 2:
        barriers.add(Barrier())
        barriers.add(Barrier())
        print(f"Score is{real_score}")
        spawn_time = 0

    if vy > 50:
        accy = g*35
    else:
        accy = g*25
    vy += accy*dt # POSITIVE DIRECTION IS DOWNWARDS
    ball_pos.y += vy*dt
    pygame.display.flip()
    dt = clock.tick(60)/10**3


pygame.quit()