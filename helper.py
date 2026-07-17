class Treenode:
    def _init_(self,val=0,right=None,left=None):
        self.value=val
        self.right=right
        self.left=left
def inorder_transversal(root):
    result=[]
    if root:
        result.extend(inorder_transversal(root.left))
        result.append(root.val)
        result.extend(inorder_transversal(root.right))
    return result
root=Treenode(1)
root.right=Treenode(2)
root.right.left=Treenode(3)
print(inorder_transversal(root))