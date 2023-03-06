def array123(nums):
  sequence = [False, False, False]
  for num in nums:
    if num == 1:
      sequence[0] = True
    elif sequence[0] == True and num == 2:
      sequence[1] = True
    elif sequence[0] == True and sequence[1] == True and num == 3:
      sequence[2] = True
    else:
      sequence = [False, False, False]
  if sequence == [True, True, True]:
    return True
  else:
    return False

array123([1, 1, 2, 3, 1])