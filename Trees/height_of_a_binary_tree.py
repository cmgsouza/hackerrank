# Tree: Height of a Binary Tree

def height(root):
    if root is None:
        return -1 
    left_value = height(root.left)
    right_value = height(root.right)
    return 1 + max(left_value, right_value)