"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # set of edges from this vertex

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) # add v2 as a neighbour to v1
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

            # If that vertex has not been visited...
            if v not in visited:
                # Visit it
                print(v)

                # Mark it visited
                visited.add(v)

                # Then add all of its neighbours to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack and add the starting vertex ID
        s = []
        s.append(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while len(s) > 0:
            # pop the fist vertex from the stack
            v = s.pop()

            # If that vertex has not been visited...
            if v not in visited:
                # Visit it
                print(v)

                # Mark it visited
                visited.add(v)

                # Then add all of its neighbours to the stack
                for neighbour in self.get_neighbors(v):
                    s.append(neighbour)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create empty stack and add the starting vertex ID
        s = []
        s.append(starting_vertex)

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # create empty queue and enqueue A PATH to the starting vertex ID
        paths = Queue()
        paths.enqueue([starting_vertex])


        visited = set()

        # while the queue is not empty...
        while paths.size() > 0:
            # pop off the next path from the queue of paths
            path = paths.dequeue()
            # grab the last vertex from the path
            vertex = path[-1]
            # if the vertex matches what we're looking for return the path
            if vertex not in visited and vertex == destination_vertex:
                # mark it as visited
                visited.add(vertex)
                return path # or print?
            else:
                for neighbor in self.get_neighbors(vertex):
                    new_path = path + [neighbor]
                    paths.enqueue(new_path)
                    visited.add(vertex)
                
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        # create empty queue and enqueue A PATH to the starting vertex ID
        paths = []
        paths.append([starting_vertex])

        visited = set()

        # while the stack is not empty...
        while len(paths) > 0:
            # pop off the next path from the queue of paths
            path = paths.pop()
            # grab the last vertex from the path
            vertex = path[-1]
            # if the vertex matches what we're looking for return the path
            if vertex not in visited and vertex == destination_vertex:
                # mark it as visited
                visited.add(vertex)
                return path # or print?
            else:
                for neighbor in self.get_neighbors(vertex):
                    new_path = path + [neighbor]
                    paths.append(new_path)
                    visited.add(vertex)
 
        
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            visited.add(starting_vertex)
            return [starting_vertex]

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                path = self.dfs_recursive(neighbor, destination_vertex, visited)
                if path:
                    return [starting_vertex] + path
                

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
