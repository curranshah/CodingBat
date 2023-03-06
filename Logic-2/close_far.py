def close_far(a, b, c):
  if abs(a-b) <= 1:
    close_val = b
  elif abs(a-c)  <= 1:
    close_val = c
  else:
    return False
  if close_val == b and abs(a-c) >= 2 and abs(b-c) >= 2:
    return True
  elif close_val == c and abs(a-b) >= 2 and abs(c-b) >= 2:
    return True
  else:
    return False