def last2(str):
  return sum(str[x:].startswith(str[-2:]) for x in range(len(str)-2))