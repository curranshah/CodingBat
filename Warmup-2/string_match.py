def string_match(a, b):
  count = 0
  for x in range(len(a)-1):
    if a[x:x+2] == b[x:x+2]:
      count += 1
  return count