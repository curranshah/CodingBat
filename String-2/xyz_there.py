def xyz_there(str):
    # count occurences of 'xyz' and count occurrences of '.xyz'.  If they are the same then False otherwise return True
    count1 = str.count('xyz')
    count2 = str.count('.xyz')
    if count1 != count2:
        return True
    else:
        return False