'''
Determine whether there is a path between two nodes in a graph

Constraints
    The graph is directed
    Assume we already have a Node and Graph class
    Assume this is a connected graph
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
        search_path(start=0, end=2) -> True
        search_path(start=0, end=0) -> True
        search_path(start=0, end=5) -> False
'''

# Implement

class GraphPathExists(Graph):

    def path_exists(self, start, end):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestPathExists(object):

    def test_path_exists(self):
        nodes = []
        graph = GraphPathExists()
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

        assert_equal(graph.path_exists(nodes[0], nodes[2]), True)
        assert_equal(graph.path_exists(nodes[0], nodes[0]), True)
        assert_equal(graph.path_exists(nodes[4], nodes[5]), False)

        print('Success: test_path_exists')


def main():
    test = TestPathExists()
    test.test_path_exists()


if __name__ == '__main__':
    main()

'''
Algorithm
    We can use DFS or BDS
    BFS can also be used to determine shortest path
    DFS is easier to implement with straight recursion
        but often results in a longer path
    We'll use BFS

    Add the start node to the queue and mark it as visited
    If the start node is the end node
        return True
    While the queue is not empty
        dequeue a node and visit it
        if the node is the end node
            return True
        Iterate through each adjacent node
            if the node has not been visited
                add it to the queue and mark it as visited
    return False

    Complexity:
        Time: O(V + E), where V = # of vertices, E = # of edged
        Space: O(V + E)
'''

# Solution
from collections import deque

class GraphPathExistsSolution(Graph):

    def path_exists(self, start, end):
        if start is None or end is None:
            return False
        if start is end:
            return True
        queue = deque()
        queue.append(start)
        start.visit_state = State.visited
        while queue:
            node = queue.popleft()
            if node is end:
                return True
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visit_state = State.visited
        return False
