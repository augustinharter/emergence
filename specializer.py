import random
import math

class Cell():
  global xfac, yfac
  def __init__(self, mutation_rate=0.1):
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

def calc_env(pop):
  xenv = sum(c.x**2 for c in pop)
  yenv = sum(c.y**2 for c in pop)
  return xenv, yenv

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

for universe in range(n_universes):
  population = [Cell(mutation_rate=0.1) for _ in range(n_cells)]
  xenv, yenv = calc_env(population)
  for epoch in range(n_epochs):
    for cell in population:
      xenv, yenv = cell.evolve(xenv, yenv)
  print(math.ceil(eval(xenv,yenv)))
  print(sum([c.x for c in population]), sum([c.y for c in population]))


while True:
  draw()
  #cv2.imshow("noisflow", cv2.resize(img,(53,30)))
  cv2.imshow("colony", img)
  key = cv2.waitKey(delay=1)
  if key == 27:
    cv2.destroyAllWindows()
    break