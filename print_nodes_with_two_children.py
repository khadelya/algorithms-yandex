class Node:
    def __init__(self,val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val,self.root)
        
    def _add(self,val,node):
        if val < node.v:
            if node.l is None:
                node.l = Node(val)
            else:
                self._add(val,node.l)
        else:
            if node.r is None:
                node.r = Node(val)
            else:
                self._add(val,node.r)
        
    def inorder_traversal(self,node):
        if node:
            self.inorder_traversal(node.l)
            if node.l and node.r:
                print(node.v)
            self.inorder_traversal(node.r)

seq = list(map(int,input().split()))
unique_elements = set()
tree = Tree()
for element in seq[:-1]:
    if element not in unique_elements:
        tree.add(element)
    unique_elements.add(element)
tree.inorder_traversal(tree.root)