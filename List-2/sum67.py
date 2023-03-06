
def sum67(nums):
    six_detected = False
    seven_detected = False
    sum = 0
    for x in range(len(nums)):
        if not six_detected:
            if nums[x] != 6:
                sum += nums[x]
            else:
                six_detected = True
        else:
            if nums[x] == 7:
                six_detected = False
    return sum

