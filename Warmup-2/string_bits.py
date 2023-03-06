def string_bits(str):
  chars = ''
  for i in range(len(str)):
    if i%2 == 0:
      chars = chars + str[i]
  return chars