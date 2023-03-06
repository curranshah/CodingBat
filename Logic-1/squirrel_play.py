def squirrel_play(temp, is_summer):
  if temp < 60:
    return False
  elif temp <= 90 and is_summer == False:
    return True
  elif temp <= 100 and is_summer == True:
    return True
  else:
    return False