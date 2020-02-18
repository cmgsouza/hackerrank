# Arrays: Left Rotation

def rotLeft(a, d):
    i = d % len(a)
    return a[i:] + a[:i]