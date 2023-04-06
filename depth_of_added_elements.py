class Node:
    def __init__(self,val):
        self.l = None
        self.r = None
        self.v = val
class Tree:
    def __init__(self):
        self.root = None
    
    def add(self,val):
        level = 1
        if self.root is None:
            self.root = Node(val)
            print(level, end = " ")
        else:
            self._add(val,self.root,level)

    def _add(self,val,node,level):
        level+=1
        if val < node.v:
            if node.l is None:
                node.l = Node(val)
                print(level, end = " ")
            else:
                self._add(val,node.l,level)
        else:
            if node.r is None:
                node.r = Node(val)
                print(level, end = " ")
            else:
                self._add(val,node.r,level)
    

seq = list(map(int,input().split()))
unique_elements = set()
tree = Tree()
for element in seq[:-1]:
    if element not in unique_elements:
        tree.add(element)
    unique_elements.add(element)
