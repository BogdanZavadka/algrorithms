from node import Node

root = Node()
root.read_nodes()
min_way = root.find_minimum_depth(root.root)
print('Min width: ', min_way[0])
root.write_to_file(min_way[1])
print('Min way: ', end='')
for i in min_way[1]:
    if min_way[1].index(i) + 1 > len(min_way[1]) - 1:
        print(i)
    else:
        print(i, end='->')
