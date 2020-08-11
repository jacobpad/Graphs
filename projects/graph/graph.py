"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Add a vertex to the graph.
        self.vertices[vertex_id] = set() # This will hold edges

    def add_edge(self, v1, v2):
        # Add a directed edge to the graph.
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) # There's an edge from v1 to v2
        else:
            raise IndexError("Vert does not exist")

    def get_neighbors(self, vertex_id):
        # Get all neighbors (edges) of a vertex.
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Print each vertex in breadth-first order beginning from starting_vertex.

        # Create empty queue
        q = Queue()

        # Init: enqueue the starting node
        q.enqueue(starting_vertex)

        # Set to keet track of visited nodes
        visited = set()

        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # If it's not yet been visited
            if v not in visited:
                # Mark as visited (add to visited set)
                visited.add(v)

                # This is where I could "DO SOMETHING" with the node ... like print
                # print(f'ZVisited {v}')
                # print(f'{v}')
                print(v)

                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    if next_vert:
                        q.enqueue(next_vert)

    def dft(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex.
        
        # Create empty stack
        s = Stack()

        # Push the starting node
        s.push(starting_vertex)

        # Set to keet track of visited nodes
        visited = set()

        # While the stack isn't empty
        while s.size() > 0:
            # Pop the first item
            v = s.pop()
            # If it's not yet been visited
            if v not in visited:
                # Mark as visited (add to visited set)
                visited.add(v)

                # This is where I could "DO SOMETHING" with the node ... like print
                # print(f'Visited {v}')
                # print(f'{v}')
                print(v)

                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    if next_vert:
                        s.push(next_vert)

    def bfs(self, starting_vertex, destination_vertex):
        # Return a list containing the shortest path from starting_vertex to
        # destination_vertex in breath-first order.

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:

            # Dequeue the first PATH
            path = q.dequeue()

            # Grab the last vertex from the PATH
            v = path[-1]

            # If that vertex has not been visited...
            if v not in visited:

                # CHECK IF IT'S THE TARGET
                if v == destination_vertex: 
                    
                  # IF SO, RETURN PATH
                  return path

                # Mark it as visited...
                visited.add(v)

                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHOR TO THE BACK
                for next_vert in self.get_neighbors(v):
                    new_path = list(path) # Copy the list
                    new_path.append(next_vert) # Add the last one to the end of the list
                    q.enqueue(new_path) # Add the new ones in

        # If we get this far, the node doesn't exist
        return None

    def dfs(self, starting_vertex, destination_vertex):
        # Return a list containing a path from starting_vertex to 
        # destination_vertex in depth-first order.
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            vertex_list = s.pop()
            vertex = vertex_list[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return vertex_list
                visited.add(vertex)
                for next_vertex in self.get_neighbors(vertex):
                    new_path = [*vertex_list]
                    if next_vertex:
                        new_path.append(next_vertex)
                        s.push(new_path)











    def dft_recursive(self, starting_vertex, visited=set()):
        # Print each vertex in depth-first order beginning from starting_vertex.
        # This should be done using recursion.
        visited.add(starting_vertex)
        print(starting_vertex)
        for val in self.vertices[starting_vertex]:
            if val not in visited:
                self.dft_recursive(val, visited)





































    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        # Return a list containing a path from starting_vertex to 
        # destination_vertex in depth-first order.
        # This should be done using recursion.
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for vertex in self.vertices[starting_vertex]:
            if vertex not in path:
                traced_path = self.dfs_recursive(vertex, destination_vertex, path)
                if traced_path:
                    return traced_path
        





















































































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
