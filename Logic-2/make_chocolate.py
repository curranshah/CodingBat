def make_chocolate(small, big, goal):
  while big > 0 and goal >= 5:
    goal = goal - 5
    big = big - 1
  small_needed = goal
  if small == goal:
    return small
  elif small > goal:
    return goal
  else:
    return -1