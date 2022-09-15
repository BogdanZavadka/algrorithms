from node import Node


class RedBlackTree:
    def __init__(self):
        self.leaf = Node(None)
        self.leaf.left = None
        self.leaf.right = None
        self.leaf.color = 'B'
        self.root = self.leaf

    def insert(self, val: int):
        if self.root == self.leaf:
            node = Node(val)
            node.parent = None
            node.left = self.leaf
            node.right = self.leaf
            node.color = 'B'
            self.root = node
        else:
            self.insert_node(self.root, val)

    def insert_node(self, root: Node, val: int):
        if val > root.val:
            if root.right == self.leaf:
                node = Node(val)
                node.parent = root
                node.left = self.leaf
                node.right = self.leaf
                node.color = 'R'
                root.right = node
                self.fix_insert(root.right)
            else:
                self.insert_node(root.right, val)
        else:
            if root.left == self.leaf:
                node = Node(val)
                node.parent = root
                node.left = self.leaf
                node.right = self.leaf
                node.color = 'R'
                root.left = node
                self.fix_insert(root.left)
            else:
                self.insert_node(root.left, val)

    def left_rotate(self, node: Node):
        child = node.right                                      
        node.right = child.left                                
        if child.left != self.leaf:
            child.left.parent = node

        child.parent = node.parent                              
        if not node.parent:                            
            self.root = child                                
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.left = node
        node.parent = child

    def right_rotate(self, node: Node):
        child = node.left                                       
        node.left = child.right                                
        if child.right != self.leaf:
            child.right.parent = node
        child.parent = node.parent                              
        if not node.parent:                            
            self.root = child                                
        elif node == node.parent.right:
            node.parent.right = child
        else:
            node.parent.left = child
        child.right = node
        node.parent = child

    def fix_insert(self, node: Node):
        while node.parent.color == 'R':                      
            if node.parent == node.parent.parent.right:        
                uncle = node.parent.parent.left                
                if uncle.color == 'R':                         
                    uncle.color = 'B'                           
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'           
                    node = node.parent.parent                   
                else:
                    if node == node.parent.left:              
                        node = node.parent
                        self.right_rotate(node)                       
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.left_rotate(node.parent.parent)
            else:                                         
                uncle = node.parent.parent.right                
                if uncle.color == 'R':                          
                    uncle.color = 'B'                          
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'             
                    node = node.parent.parent                   
                else:
                    if node == node.parent.right:               
                        node = node.parent
                        self.left_rotate(node)                        
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.right_rotate(node.parent.parent)              
            if node == self.root:                            
                break
        self.root.color = 'B'                               

    def traversal(self, root: Node):
        if root:
            self.traversal(root.left)
            if root.val:
                print(root.val, root.color)
            self.traversal(root.right)
