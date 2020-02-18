def twoStrings(s1, s2):
    lis = [i for i in s1 if i in s2]
    if len(lis) != 0:
        return "YES"
    else:
        return "NO"
