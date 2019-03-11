'''
Implement depth-first search on a graph

Constraints
    The graph is directed
    Assume we already have a Graph and Node class
    Assume inputs are valid
    Assume this is a connected graph
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
        Order of nodes visited: [0, 1, 3, 2, 4, 5]
'''
# Implement
class GraphDfs(Graph):

    def dfs(self, root, visit_func):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestDfs(object):

    def __init__(self):
        self.results = Results()

    def test_dfs(self):
        nodes = []
        graph = GraphDfs()
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
        graph.dfs(nodes[0], self.results.add_result)
        assert_equal(str(self.results), "[0, 1, 3, 2, 4, 5]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()

'''
Algorithm
    If we want to visit every node in a graph, we generally prefer DFS
    since its simpler (no need to use a queue)

    Visit the current node and mark it visited
    Iterate through each adjacent node
        If the node has not been visited
            Call dfs on it

    Complexity:
        Time: O(V + E), where V = number of vertices and E = number of edges
        Space: O(V), for the recursion depth
'''

# Solution
class GraphDfsSolution(Graph):

    def dfs(self, root, visit_func):
        if root is None:
            return
        visit_func(root)
        root.visit_state = State.visited
        for node in root.adj_nodes.values():
            if node.visit_state == State.unvisited:
                self.dfs(node, visit_func)
