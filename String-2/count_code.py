def count_code(str):
  counter = 0
  for i in range(len(str)-3):
    if str[i] == 'c':
      if str[i+1] == 'o':
        if str[i+3] == 'e':
          counter += 1
  return counter