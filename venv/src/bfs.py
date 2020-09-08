from node import Node

def bfs(map, start, end):

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[0])) or \
                    node_position[1] < 0:
                continue

            if map[node_position[0], node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:

            if child not in closed_list:
                closed_list.append(child)
                open_list.append(child)



    print 'failure'



