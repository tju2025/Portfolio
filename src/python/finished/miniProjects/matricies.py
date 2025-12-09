import sys
import pygame
from math import *
from pygame.constants import K_s

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

angle_x = angle_y = angle_z = 90

projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]



cube_points = [n for n in range(8)]
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]

def multiply_m(a, b):
  a_rows = len(a)
  a_cols = len(a[0])

  b_rows = len(b)
  b_cols = len(b[0])

  product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

  if a_cols == b_rows:
    for i in range(a_rows):
      for j in range(b_cols):
        for k in range(b_rows):
          product[i][j] += a[i][k] * b[k][j]

  else:
    print("INCOMPATIBLE MATRIX SIZES")

  return product

scale=100

def update(pressed_keys, angle_x, angle_y, scale):
  if pressed_keys[K_RSHIFT] or pressed_keys[K_LSHIFT]:
    mult = 5
  else:
    mult = 1
  if pressed_keys[K_UP]:
    angle_x += 0.01*mult
  if pressed_keys[K_DOWN]:
    angle_x -= 0.01*mult
  if pressed_keys[K_RIGHT]:
    angle_y += 0.01*mult
  if pressed_keys[K_LEFT]:
    angle_y -= 0.01*mult
  if pressed_keys[K_w]:
    scale += 0.5*mult
  if pressed_keys[K_s]:
    scale -= 0.5*mult
  if pressed_keys[K_r]:
    angle_x = angle_y = 0
    scale = 100
  if pressed_keys[K_SPACE]:
    print(angle_x, angle_y, scale)
  return angle_x, angle_y, scale
  
from pygame.locals import (
  K_UP,
  K_DOWN,
  K_RIGHT,
  K_LEFT,
  K_ESCAPE,
  KEYDOWN,
  QUIT,
  RLEACCEL,
  K_r,
  K_RSHIFT,
  K_LSHIFT,
  K_w,
  K_s,
  K_SPACE,
)

def connect_points(i, j, points, mode=False, *pointNums):
  if mode == False:
    pygame.draw.line(window, (255, 255, 255), (points[i]), (points[j]))
  else:
    mid_x1 = (points[pointNums[0]][0] + points[pointNums[1]][0])/2
    mid_y1 = (points[pointNums[0]][1] + points[pointNums[1]][1])/2
    mid_x2 = (points[pointNums[2]][0] + points[pointNums[3]][0])/2
    mid_y2 = (points[pointNums[2]][1] + points[pointNums[3]][1])/2
    pygame.draw.line(window, (0, 255, 0), (mid_x1, mid_y1), (mid_x2, mid_y2))
    
#Main loop
while True:
  clock.tick(60)
  window.fill((0, 0, 0))
  rotation_matrix_x = [[1, 0, 0], 
     [0, cos(angle_x), -sin(angle_x)],
     [0, sin(angle_x), cos(angle_x)]]

  rotation_matrix_y = [[cos(angle_y), 0, sin(angle_y)], 
     [0, 1, 0],
     [-sin(angle_y), 0, cos(angle_y)]]

  rotation_matrix_z = [[cos(angle_z), -sin(angle_z), 0],
     [sin(angle_z), cos(angle_z), 0],
     [0, 0, 1]]

  points = [0 for _ in range(len(cube_points))]
  i = 0

  for point in cube_points:
    rotated_x = multiply_m(rotation_matrix_x, point)
    rotated_y = multiply_m(rotation_matrix_y, rotated_x)
    rotated_z = multiply_m(rotation_matrix_x, rotated_y)
    point_2d = multiply_m(projection_matrix, rotated_z)
    x = (point_2d[0][0] * scale) + window.get_width()//2
    y = (point_2d[1][0] * scale) + window.get_height()//2

    points[i] = (x,y)
    i += 1
    pygame.draw.circle(window, (255, 0, 0), (x, y), 0.05*scale if scale > 60 else 3)

  connect_points(0, 1, points)
  connect_points(0, 3, points)
  connect_points(0, 4, points)
  connect_points(1, 2, points)
  connect_points(1, 5, points)
  connect_points(2, 3, points)
  connect_points(2, 6, points)
  connect_points(3, 7, points)
  connect_points(4, 5, points)
  connect_points(4, 7, points)
  connect_points(6, 5, points)
  connect_points(6, 7, points)
  #experimental lines
  connect_points(6, 7, points, True, 0, 1, 2, 3)
  #connect_points(6, 7, points, True, 0, 1, 2, 4)
  #connect_points(6, 7, points, True, 0, 0, 6, 6)
  #connect_points(6, 7, points, True, 0, 0, 2, 1)
  #connect_points(6, 7, points, True, 2, 1, 2, 2)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  pressed_keys = pygame.key.get_pressed()
  angle_x, angle_y, scale = update(pressed_keys, angle_x, angle_y, scale)
  
  pygame.display.update()