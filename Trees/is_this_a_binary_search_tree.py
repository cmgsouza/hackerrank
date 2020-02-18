def unique_and_sorted(lis): 
    return sorted(list(set(lis)))

def inorder_print(start, traversal):
    """Left -> Root -> Right """
    if start: # check if start node is None
        traversal = inorder_print(start.left, traversal)
        traversal += str(start.data) + " "
        traversal = inorder_print(start.right, traversal)
    return traversal

def checkBST(root):
    s = inorder_print(root, "")
    lis = list(map(lambda x: int(x), s.split()))
    return lis == unique_and_sorted(lis)