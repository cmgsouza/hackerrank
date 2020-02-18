# Alternating Characters

def alternatingCharacters(s):
    l = []
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            l.append(s[i])
    return len(l)