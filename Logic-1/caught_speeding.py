def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    new_speed = speed - 5
    if new_speed <= 60:
      return 0
    elif new_speed >= 61 and new_speed <= 81:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed >= 61 and speed <= 81:
      return 1
    else:
      return 2