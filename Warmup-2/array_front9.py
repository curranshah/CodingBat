def array_front9(nums):
  for x in range(len(nums)):
    if x <= 3:
      if nums[x] == 9:
        return True
  return False