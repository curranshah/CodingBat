def fix_teen(n):
    if n == 15 or n == 16:
        return n
    else:
        return 0

def no_teen_sum(a, b, c):
    list1 = [a, b, c]
    sum = 0
    for x in range(len(list1)):
        if list1[x] >= 13 and list1[x] <= 19:
            n = fix_teen(list1[x])
            sum += n
        else:
            sum += list1[x]

    return sum