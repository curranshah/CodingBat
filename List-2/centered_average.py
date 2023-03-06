def centered_average(nums):
  for x in range(len(nums)):
    if x == 0:
      max = nums[x]
      min = nums[x]
    elif nums[x] > max:
      max = nums[x]
    elif nums[x] < min:
      min = nums[x]
  nums.remove(min)
  nums.remove(max)
  return sum(nums)/len(nums)