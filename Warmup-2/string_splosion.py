def string_splosion(str):
  final = ''
  for x in range(len(str)):
    sub = str[:x]
    final += sub
  final += str
  return final