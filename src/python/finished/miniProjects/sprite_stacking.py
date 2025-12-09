import sys
import os
import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), 0)
display = pygame.Surface((100, 100))

images = [pygame.image.load('Sprites/' + img) for img in os.listdir('Sprites')]

for i in range(0, len(images)):
  images[i] = pygame.transform.scale(images[i], (6, 6))
images = images[::-1]
clock = pygame.time.Clock()


def render_stack(surf, images, pos, rotation, spread=1.0):
  for i, img in enumerate(images):
    rotated_img = pygame.transform.rotate(img, rotation)
    surf.blit(rotated_img,
              (pos[0] - rotated_img.get_width() // 2,
               pos[1] - rotated_img.get_height() // 2 - i * spread))


#used as rotation for render_stack
frame = 0
spread = 2.0


def update(pressed_keys, fr, sp=2.0):
  #allow for real time changing of rotation and spread
  if pressed_keys[K_UP]:
    sp += 0.1
  if pressed_keys[K_DOWN]:
    sp -= 0.1
  if pressed_keys[K_RIGHT]:
    fr -= 1
  if pressed_keys[K_LEFT]:
    fr += 1
  if pressed_keys[K_SPACE]:
    print("Spread", sp, "Frame", fr)
  return fr, sp


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
    K_SPACE,
)

while True:
  display.fill((255, 255, 255))

  render_stack(display, images, (50, 50), frame, spread)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  pressed_keys = pygame.key.get_pressed()
  frame, spread = update(pressed_keys, frame, spread)

  screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
  pygame.display.update()
  clock.tick(60)
