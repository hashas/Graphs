"""
Assumptions
-----------
- input not empty
- no cycles in the input
- no repeated ancestors i.e. any two individuals are connected by one path
- IDs always positive integers
- parent may have any number of children
- if ID has no parent, function should return -1
"""
#test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#
#ancestors = {
#        1: {10},
#        2: {-1},
#        3: {1, 2},
#        4: {-1},
#        5: {4},
#        6: {3, 5},
#        7: {5, 8},
#        8: {4, 11},
#        9: {8},
#        10: {-1},
#        11: {-1}
#}

# I tried to implement a recursive solution but had difficulties so commented out
#def get_neighbors(data, vertex_id):
#    return data[vertex_id]
#
#
#def earliest_ancestor(ancestors, starting_node, visited=set(), curr_path=[]):
#
#    if starting_node not in visited:
#        curr_path.append(starting_node)
#        visited.add(starting_node)
#        for neighbor in get_neighbors(ancestors, starting_node):
#            if neighbor < 0:
#                return curr_path
#            else:
#                earliest_ancestor(ancestors, neighbor, visited, curr_path)
    

def earliest_ancestor(ancestors, starting_node):

    vertices = {}

    def add_relationship(pair):
        for node in pair:
            add_vertex(node)
        add_edge(*pair)

    def add_vertex(v):
        if v not in vertices:
            vertices[v] = set()

    def add_edge(ancestor, child):
        vertices[child].add(ancestor)
    # populate our graph
    for pair in ancestors:
        add_relationship(pair)
    oldest_ancestor = -1
    max_length = 0
    if not len(vertices[starting_node]):
        return oldest_ancestor
    visited = set()
    stack = []
    current = starting_node
    # until stack is empty and current has no unvisited neighbours
    stack.append(starting_node)
    while len(stack):
        # visit current vertex if it wasn't visited
        if current not in visited:
            visited.add(current)
        # look for unvisited neighbours
        unvisited_neighbours = [
            v for v in vertices[current] if v not in visited]
        if unvisited_neighbours:
            # If it has an unvisited neighbour, push current vertex on stack, make neighbour current
            stack.append(current)
            current = unvisited_neighbours[0]
        else:
            # If it has no unvisited neighbors, pop off stack and set as current
            if len(stack) >= max_length:
                # do depth first traversal of the graph
                # each time we have to go back, compare against max length
                # if bigger, put current ancestor as oldest
                oldest_ancestor = current
                max_length = len(stack)
            current = stack.pop()
    return oldest_ancestor

"""
data = [ (parent, child), (parent, child) ]

function(data, ID):
if more than one ancestor tied for "earliest":
return one with the lowest numeric ID

if ID has no parents:
return -1





    return earliest ancestor (i.e. farthest distance from the input ID)
"""
