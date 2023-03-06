def double_char(str):
  chars = [x for x in str]
  new_string = ''
  for char in chars:
    new_string += char
    new_string += char
  return new_string