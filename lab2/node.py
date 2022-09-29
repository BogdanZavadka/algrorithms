class Node:
    contains_deepest_element = False
    way = []

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
        self.root = None

    def read_nodes(self):
        with open('input.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        for i in range(len(lines)):
            if i == 0:
                self.insert(int(lines[i]))
            else:
                self.insert(int(lines[i][0]), int(lines[i][2]))

    def insert(self, first_node: int, second_node: int = None):
        if not second_node:
            self.root = Node(first_node)
        else:
            self.insert_nodes(first_node, second_node, self.root)

    def insert_nodes(self, first_node: int, second_node: int, node):
        if node:
            self.insert_nodes(first_node, second_node, node.left)
            if node.value == first_node:
                if not node.left:
                    node.left = Node(second_node)
                else:
                    node.right = Node(second_node)
            self.insert_nodes(first_node, second_node, node.right)

    def find_minimum_path(self, current_node, search_node):
        if current_node:
            self.find_minimum_path(current_node.left, search_node)
            self.check(current_node, search_node)
            if self.contains_deepest_element:
                self.way.append(current_node.value)
                self.contains_deepest_element = False
            self.find_minimum_path(current_node.right, search_node)

    def check(self, current_node, search_node):
        if current_node:
            self.check(current_node.left, search_node)
            if current_node == search_node:
                self.contains_deepest_element = True
            self.check(current_node.right, search_node)

    def find_minimum_depth(self, root):
        queue = []
        queue.append({'node': root, 'depth': 1})
        while queue:
            item = queue.pop(0)
            current_node = item['node']
            current_depth = item['depth']
            if not current_node.left and not current_node.right:
                self.find_minimum_path(root, current_node)
                return [current_depth, self.way]
            if current_node.left:
                queue.append({'node': current_node.left, 'depth': current_depth + 1})
            if current_node.right:
                queue.append({'node': current_node.right, 'depth': current_depth + 1})

    def write_to_file(self, way: []):
        way.reverse()
        min_way = 'Min way: '
        for i in way:
            if way.index(i) + 1 > len(way) - 1:
                min_way += str(i)
            else:
                min_way += str(i) + '->'
        with open('output.txt', 'w') as output_file:
            output_file.write(min_way)
