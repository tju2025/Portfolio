import pygame
import sys
import time  # Test if inputs are registering; time.sleep, test for input
import random

# THIS IS NOT MY CREATION. I FOUND IT ONLINE AND MODIFIED IT SLIGHTLY (for learning purposes)
# https://realpython.com/pygame-a-primer/#a-simple-jet-game

# Import pygame.locals for easier access to key coordinates. Instead of having to type pygame.K_UP, you can just type K_UP
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
)

# Define constants for screen width/height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


# Defining the Player sprite
class Player(pygame.sprite.Sprite):

  def __init__(self):
    super(Player, self).__init__()
    ##surf = pygame.Sur... but for class
    ##self.surf = pygame.Surface((75, 25))
    ##self.surf.fill((255, 255, 255))
    #convert optimises surf, faster blit()
    self.surf = pygame.image.load("rescources/sprites/Jet.png").convert()
    #set_colourkey means this RGB value should be represented as
    #transparent
    self.surf.set_colorkey((255, 255, 255), RLEACCEL)
    self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2,
                                           SCREEN_HEIGHT / 2))

  def update(self, pressed_keys):
    #moving rects based on pressed keys
    if pressed_keys[K_UP]:
      self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
      self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
      self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
      self.rect.move_ip(5, 0)
    #Keeping rect within screen boundaries
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
      self.rect.right = SCREEN_WIDTH


# Creating the enemy class
class Enemy(pygame.sprite.Sprite):

  def __init__(self):
    super(Enemy, self).__init__()
    #self.surf = pygame.Surface((20, 10)) # Make sure arg is a tuple
    #self.surf.fill((125, 125, 125))
    self.surf = pygame.image.load("rescources/sprites/Missle.png").convert()
    self.surf.set_colorkey((246, 246, 246), RLEACCEL)
    self.rect = self.surf.get_rect(
        center=(SCREEN_WIDTH * random.uniform(1.02, 1.12),
                SCREEN_HEIGHT * random.uniform(0.00, 1.00)))
    self.speed = random.randint(5, 20)

  def update(self):
    self.rect.move_ip(-(self.speed), 0)
    if self.rect.right < 0:
      self.kill()


# Creating a background image class
class Asteroid(pygame.sprite.Sprite):

  def __init__(self):
    super(Asteroid, self).__init__()
    self.surf = pygame.image.load("rescources/sprites/Asteroid.jpg")
    self.surf.set_colorkey((255, 255, 255), RLEACCEL)
    self.rect = self.surf.get_rect(
        center=(SCREEN_WIDTH * random.uniform(0.75, 1.12),
                SCREEN_HEIGHT * random.uniform(-2.00, 0.50)))
    self.speed = random.randint(20, 100)

  def update(self):
    self.rect.move_ip(-(self.speed), self.speed)
    if self.rect.right < 0 or self.rect.top > SCREEN_HEIGHT:
      self.kill()


# Initialise pygame
pygame.init()

# Create screen object
# Size determined by constants above
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creating custom events for the event handler to deal with
# Internally, pygame defines events as integers and reserves the last
# event as USEREVENT
# USEREVENT + 1 ensures a new event is being created
ADDENEMY = pygame.USEREVENT + 1
# Now we need to add the event to the event queue in regular intervals
# which is the purpose of set_timer. The 2nd argument is the interval in milliseconds
pygame.time.set_timer(ADDENEMY, 250)
ADDASTEROID = pygame.USEREVENT + 2
pygame.time.set_timer(ADDASTEROID, 1000)
# Adding a game frame rate system
clock = pygame.time.Clock()

# Instantising the player object
player = Player()

# Creating sprite groups to hold sprites
# - enemies used for collision detection and position updates
# - all_sprites used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
asteroids = pygame.sprite.Group()

# Setting up main loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    # Quitting
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        running = False
    elif event.type == QUIT:
      running = False
    elif event.type == ADDENEMY:
      new_enemy = Enemy()
      enemies.add(new_enemy)
      all_sprites.add(new_enemy)
    elif event.type == ADDASTEROID:
      new_asteroid = Asteroid()
      asteroids.add(new_asteroid)
      all_sprites.add(new_asteroid)

  # Fill screen black
  screen.fill((0, 0, 0))
  "old text 1"
  # Get all currently pressed keys
  pressed_keys = pygame.key.get_pressed()
  player.update(pressed_keys)
  # Update all sprites in the enemies sprite group
  enemies.update()
  asteroids.update()

  # Draw everything on screen
  for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)

  # Check if any enemy has collided with the player
  if pygame.sprite.spritecollideany(player, enemies):
    player.kill()
    running = False

  # Update display
  pygame.display.flip()
  # Setting the frame rate to 30
  clock.tick(30)
