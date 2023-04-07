class Node:
    def __init__(self,val):
        self.l = None
        self.r = None
        self.v = val

    def __str__(self):
        return str(self.v)

class Tree:
    def __init__(self):
        self.root = None
        self.second_max = None

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
            ordered_list.append(node.v)
            self.inorder_traversal(node.r)

seq = list(map(int,input().split()))
unique_elements = set()
tree = Tree()
ordered_list = []
for element in seq[:-1]:
    if element not in unique_elements:
        tree.add(element)
    unique_elements.add(element)
tree.inorder_traversal(tree.root)
print(ordered_list[-2])