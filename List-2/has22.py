def has22(nums):
    two_detected = False
    max_x = len(nums) - 1
    print(max_x)
    for x in range(len(nums)):
        if x != max_x:
            if nums[x] == 2:
                two_detected = True
            else:
                two_detected = False
            if two_detected and nums[x+1] == 2:
                return True
    return False

has22([1,2,1,2])