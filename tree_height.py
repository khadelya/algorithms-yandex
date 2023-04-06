class Node:
    def __init__(self,val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None
        self.height = None

    def add(self,val):
        self.height = 1
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val,self.root)
        

    def _add(self,val,node):
        self.height +=1
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

seq = list(map(int,input().split()))
unique_elements = set()
tree = Tree()
max_height = 0
for element in seq[:-1]:
    if element not in unique_elements:
        tree.add(element)
        max_height = max(max_height,tree.height)
    unique_elements.add(element)
print(max_height)
