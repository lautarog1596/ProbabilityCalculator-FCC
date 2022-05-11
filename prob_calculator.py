import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)
     
  def draw(self, num_balls):
    if num_balls > len(self.contents):
      return self.contents
    balls = []
    for i in range(num_balls):
      random_ball = random.randint(0,(len(self.contents)-1))
      balls.append(self.contents[random_ball])
      self.contents.remove(self.contents[random_ball])
    return balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
      another_hat = copy.deepcopy(hat)
      balls_drawn = another_hat.draw(num_balls_drawn)
      balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
      m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments
