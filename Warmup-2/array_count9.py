def array_count9(nums):
    count = 0
    for x in range(len(nums)):
        if nums[x] == 9:
            count += 1

    return count