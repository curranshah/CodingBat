def big_diff(nums):
  for x in range(len(nums)):
    if x == 0:
      max = nums[x]
      min = nums[x]
    elif nums[x] > max:
      max = nums[x]
    elif nums[x] < min:
      min = nums[x]
  return max - min