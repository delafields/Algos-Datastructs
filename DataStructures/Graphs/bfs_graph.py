'''
Implement a breadth-first search on a graph

Constraints
    The graph is directed
    Assume we have a Graph and Node class
    Assume it is a connected graph
    Assume inputs are valid
    Assume it fits in memory

Test Cases
    Input:
        add_edge(source, destination, weight)
            graph.add_edge(0, 1, 5)
            graph.add_edge(0, 4, 3)
            graph.add_edge(0, 5, 2)
            graph.add_edge(1, 3, 5)
            graph.add_edge(1, 4, 4)
            graph.add_edge(2, 1, 6)
            graph.add_edge(3, 2, 7)
            graph.add_edge(3, 4, 8)
    Result:
        Order of nodes visited: [0, 1, 4, 5, 3, 2]
'''

# Implement

class GraphBfs(Graph):

    def bfs(self, root, visit_func):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestBfs(object):

    def __init__(self):
        self.results = Results()

    def test_bfs(self):
        nodes = []
        graph = GraphBfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.bfs(nodes[0], self.results.add_result)
        assert_equal(str(self.results), "[0, 1, 4, 5, 3, 2]")

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()

'''
Algorithm
    We generally use a BFS to determine the shortest path

    Add the current node to the queue and mark it as visited
    While the queue is not empty
        Dequeue a node and visit it
        Iterate through each adjacent node
            If the node has not been visited
                Add it to the queue and mark it as visited

    Complexity:
        Time: O(V + E), where V = # of vertices and E = # of edges
        Space: O(V)

        Note:
            When the number of vertices in the graph is known ahead of time
                and additional data structures are used to determine which
                vertices have already been added to the queue, the space
                complexity can be expressed as O(V)
            If the graph is represented by an adjacency list
                it occupies O(V + E) space in memory
            If the graph is represented by an adjacency matrix
                it occupies O(V^2) space in memory
'''

# Solution
from collections import deque

class GraphBfsSolution(Graph):

    def bfs(self, root, visit_func):
        if root is None:
            return None
        queue = deque()
        queue.append(root)
        root.visit_state = State.visited
        while queue:
            node = queue.popleft()
            visit_func(node)
            for adjacent_node in node.adj_nodes.values():
                if adjacent_node.visit_state == State.unvisited:
                    queue.append(adjacent_node)
                    adjacent_node.visit_state = State.visited
