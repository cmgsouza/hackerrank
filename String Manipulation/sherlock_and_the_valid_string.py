#  Sherlock and the Valid String

def isValid(s):
    c = Counter(s)
    l = list(c.values())
    m = Counter(l)
    if len(m.items()) > 2:
        return "NO"
    elif len(m.items()) == 1:
        return "YES"
    else:
        frequency = sorted(list(m.keys()))
        min_frequency, max_frequency = frequency[0], frequency[1]
        min_dist_letter, max_dist_letter = m[min_frequency], m[max_frequency]
        if (min_frequency == 1 and min_dist_letter == 1) or (max_frequency == (min_frequency + 1) and max_dist_letter == 1):
            return "YES"
        else:
            return "NO"