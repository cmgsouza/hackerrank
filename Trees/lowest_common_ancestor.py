# Binary Search Tree : Lowest Common Ancestor

def lca(root, v1, v2):
    if root is None: 
        return None
  
    if root.info > v1 and root.info > v2: #  lca is left if both v1 and v2 are smaller than root    	
        return lca(root.left, v1, v2) 

    if(root.info < v1 and root.info < v2): #  lca is right if both v1 and v2 are greater than root   
        return lca(root.right, v1, v2) 
  
    return root