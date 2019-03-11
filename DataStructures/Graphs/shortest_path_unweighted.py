'''
Find the shortest path between two nodes in an unweighted graph

Constraints
    The graph is directed
    The graph is unweighted
    Assume we already have a Node and Graph class
    There are two input Nodes
    The output is a list of Node keys that make up the shortest path
    If there is no path, return None
    Assume this is a connected graph
    Assume inputs are valid
    Assume it fits in memory

Test Cases
    Input:
        add_edge(source, destination, weight)
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)
    Result:
        search_path(start=0, end=2) -> [0, 1, 3, 2]
        search_path(start=0, end=0) -> [0]
        search_path(start=4, end=5) -> None
'''

# Implement
class GraphShortestPath(Graph):

    def shortest_path(self, source_key, dest_key):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestShortestPath(object):

    def test_shortest_path(self):
        nodes = []
        graph = GraphShortestPath()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)

        assert_equal(graph.shortest_path(nodes[0].key, nodes[2].key), [0, 1, 3, 2])
        assert_equal(graph.shortest_path(nodes[0].key, nodes[0].key), [0])
        assert_equal(graph.shortest_path(nodes[4].key, nodes[5].key), None)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()

'''
Algorithm:
    To determine the shortest path in an unweighted graph, we can use BFS
    keeping track of the previous nodes ids for each node
    Previous nodes ids can be a dict of
        key: current node id
        value: previous node id

    If the start node is the end node
        return True
    Add the start node to the queue and mark it as visited
        Update the previous node ids, the previous node id of the start node is None
    While the queue is not empty
        Dequeue a node and visit it
        If the node is the end node
            return the previous nodes
        Set the previous node to the current node
        Iterate through each adjacent node
            If the node has not been visited
                Add it to the queue and mark it as visited
                Update the previous node ids
    Return None
    Walk the previous node ids backwards to get the path

    Complexity:
        Time: O(V + E), where V is the number of vertices, E is the number of edges
        Space: O(V + E)
'''

# Solution
from collections import deque

class GraphShortestPath(Graph):

    def shortest_path(self, source_key, dest_key):
        if source_key is None or dest_key is None:
            return None
        if source_key is dest_key:
            return [source_key]
        prev_node_keys = self._shortest_path(source_key, dest_key)
        if prev_node_keys is None:
            return None
        else:
            path_ids = [dest_key]
            prev_node_key = prev_node_keys[dest_key]
            while prev_node_key is not None:
                path_ids.append(prev_node_key)
                prev_node_key = prev_node_keys[prev_node_key]
            return path_ids[::-1]

    def _shortest_path(self, source_key, dest_key):
        queue = deque()
        queue.append(self.nodes[source_key])
        prev_node_keys = {source_key: None}
        self.nodes[source_key].visit_state = State.visited
        while queue:
            node = queue.popleft()
            if node.key is dest_key:
                return prev_node_keys
            prev_node = node
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    prev_node_keys[adj_node_key] = prev_node.key
                    adj_node.visit_state = State.visited
        return None
