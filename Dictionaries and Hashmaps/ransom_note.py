# Hash Tables: Ransom Note

from collections import Counter

def checkMagazine(magazine, note):
    magazine, note = Counter(magazine.split()), Counter(note.split())
    l = []
    for i, j in note.items():
        if i in magazine.keys() and j <= magazine[i]:
            l.append(i)
    if len(l) == len(note):
        print("Yes")
    else:
        print("No")