# Strings: Making Anagrams

from collections import Counter 

def makeAnagram(a, b):
    x = Counter(a)
    y = Counter(b)
    total_elements = sum(list(x.values()) + list(y.values()))
    l, m = [], []
    for i, j in x.items():
        if i in y.keys():
            l.append(i)
            m.append(max(x[i], y[i]) - abs(x[i] - y[i]))
    return total_elements - 2*sum(m)
