import cv2
import numpy as np
import random
import math

# GLOBALS
WIDTH = 300
HEIGHT = 300


class Cell():
  def __init__(self, mutation_rate=0.1):
    self.horizon = 10
    self.pos = np.array([random.random()*HEIGHT, random.random()*WIDTH])
    self.seed = random.random()*100
    self.x = random.random()
    self.y = 1-self.x
    self.mutation_rate = mutation_rate

  def evolve(self, xenv, yenv):
    d = self.mutation_rate*random.random()

    pxd = min(self.x+d, 1)
    pyd = 1-pxd
    pxnew = xenv+(-self.x**2+pxd**2)
    pynew = yenv+(-self.y**2+pyd**2)

    xd = max(self.x-d, 0)
    yd = 1-xd
    xnew = xenv+(-self.x**2+xd**2)
    ynew = yenv+(-self.y**2+yd**2)

    pos = eval(pxnew, pynew)
    neg = eval(xnew, ynew)
    if pos > neg :
      self.x = pxd
      self.y = pyd
      return pxnew, pynew
    else:
      self.x = xd
      self.y = yd
      return xnew, ynew

  def live(self):
    env = get_env(self)
    



def calc_env(pop):
  xenv = sum(c.x**2 for c in pop)
  yenv = sum(c.y**2 for c in pop)
  return xenv, yenv

def get_env(m):
  env = []
  for c in population:
    if c != m:
      continue
    diff = m.pos-c.pos
    dist = np.linalg.norm(diff)
    if dist<m.horizon:
      env.append((dist, diff[0], diff[1]))

  return np.array(env)


def eval(x, y):
  if x<0 or y<0:
    return 0
  xfac, yfac = 2, 1
  together = xfac+yfac
  return x**(xfac/together) * y**(yfac/together)

# SCRIPT #
n_universes = 100
n_epochs = 10
n_cells = 10
population = [Cell(mutation_rate=0.1) for _ in range(n_cells)]
img = np.zeros((HEIGHT,WIDTH))

while True:
  for cell in population:
    cell.live()
  cv2.imshow("colony", img)
  key = cv2.waitKey(delay=1)
  if key == 27:
    cv2.destroyAllWindows()
    break