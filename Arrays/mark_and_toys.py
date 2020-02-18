# Mark and Toys

def maximumToys(prices, k):        
    edited_lis = sorted([i for i in prices if i <= k])
    m = []
    for i in edited_lis:
        m.append(i)
        print(m, sum(m))
        if sum(m) > k:
            break
    if sum(m) >= k:
        m.pop(-1)
    return len(m)