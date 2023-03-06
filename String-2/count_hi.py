def count_hi(str):
    counter = 0
    for i in range(len(str)-1):
        if str[i] == 'h':
            if str[i+1] == 'i':
                counter +=1
    return counter

def count_hi(str):
    return str.count('hi')