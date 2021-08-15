class Tree(object):
    def __init__(self, root=None, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right
        
    def is_leaf(self):
        return not(self.left or self.right)
        
    def __str__(self):
        if self.is_leaf():
            return f'[{self.root}]'
        return f'[{self.left or "_"} {self.root} {self.right or "_"}]'
    
    def __eq__(self, other):
        return self == other
    
    def __ne__(self, other):
        return not (self == other)

class Node(object):
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return str(self.value)   
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value 

    def __ne__(self, other):
        return self.value != other.value 
