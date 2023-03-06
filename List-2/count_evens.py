def count_evens(nums):
  counter = 0
  for x in range(len(nums)):
    if nums[x]%2 == 0:
      counter += 1
  return counter