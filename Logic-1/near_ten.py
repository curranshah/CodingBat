def near_ten(num):
  remainder = num % 10
  if remainder <= 2 or remainder >= 8:
    return True
  else:
    return False