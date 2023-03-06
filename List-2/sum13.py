


def sum13(nums):
    if len(nums) == 0:
        return 0
    sum = 0
    num_detector = False
    for x in range(len(nums)):
        if nums[x] != 13:
            if not num_detector:
                sum += nums[x]
            num_detector = False
        else:
            num_detector = True
    return sum

sum13([1,2,13,2,1,13])