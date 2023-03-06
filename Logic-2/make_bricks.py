def make_bricks(small, big, goal):
    max_length = small + 5*big
    if max_length >= goal:
      if small >= goal:
        return True
      elif int(goal/5) >= goal:
        if goal%5 <= small:
            return True
        else:
            return False
      elif int(goal/5) < goal:
        if goal - 5*int(goal/5) <= small:
            return True
        else:
            return False
    else:
      return False