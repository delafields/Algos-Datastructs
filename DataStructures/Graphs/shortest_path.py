'''
Find the shortest path between two nodes in a graph

Constraints
    The graph is directed
    The graph can have cycles
        If it didn't, it would be a DAG and we could use a topological sort
    The edges are weighted
        If they weren't we could do a BFS
    The edges are all non-negative numbers
        If they could be negative, we could use Bellman-Ford
        Graphs with negative cost cycles do not have a defined shortest path
    Do not have to check for non-negative edges
    Assume it is a connected graph
    Assume inputs are valid
    Assume we already have a Priority Queue and Graph class
    Assume this fits in memory

Test Cases
    The constraints state we don't have to check for negative edges, so we test with the general case
        graph.add_edge('a', 'b', weight=5)
        graph.add_edge('a', 'c', weight=3)
        graph.add_edge('a', 'e', weight=2)
        graph.add_edge('b', 'd', weight=2)
        graph.add_edge('c', 'b', weight=1)
        graph.add_edge('c', 'd', weight=1)
        graph.add_edge('d', 'a', weight=1)
        graph.add_edge('d', 'g', weight=2)
        graph.add_edge('d', 'h', weight=1)
        graph.add_edge('e', 'a', weight=1)
        graph.add_edge('e', 'h', weight=4)
        graph.add_edge('e', 'i', weight=7)
        graph.add_edge('f', 'b', weight=3)
        graph.add_edge('f', 'g', weight=1)
        graph.add_edge('g', 'c', weight=3)
        graph.add_edge('g', 'i', weight=2)
        graph.add_edge('h', 'c', weight=2)
        graph.add_edge('h', 'f', weight=2)
        graph.add_edge('h', 'g', weight=2)
        shortest_path = ShortestPath(graph)
        result = shortest_path.find_shortest_path('a', 'i')
        assert_equal(result, ['a', 'c', 'd', 'g', 'i'])
        assert_equal(shortest_path.path_weight['i'], 8)
'''

# Implement
class ShortestPath:

    def __init__(self, graph):
        # TODO: Implement me
        pass

    def find_shortest_path(self, start_node_key, end_node_key):
        # TODO: Implement me
        pass

# Unit Tests


'''
![gif of algo](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)
Algorithm:

    Initialize the following:
        previous = {} # Key: node key, Val: prev node key, shortest path
            Set each node's previous node key to None
        path_weight = {} # Key: node key, Val: weight, shortest path
            Set each node's shortest path weight to infinity
        remaining = PriorityQueue() # Queue of node key, path weight
            Add each node's shortest path weight to the PriorityQueue

        Set the node's path_weight to 0 and update the value in remaining
        Loop while remaining still has items
            Extract the min node (node with minimum path weight) from remaining
            Loop through each adjacent node in the min node
                Calculate the new weight
                    Adjacent node's edge weight + the min node's path_weight
                If the newly calculated path is less than the adjacent node's current path_weight
                    Set the node's previous node key leading to the shortest path
                    Update the adjacent node's shortest path and update the value in the PriorityQueue
        Walk backwards to determine the shortest path
            Start at the end node, walk the previous dict to get to the start node
        Reverse the list and return it

        Complexity for array-based priority queue:
            Time: O(V^2) where V is the number of vertices
            Space: O(V^2)
            Note:
                This is beter than the min-heap-based variant if the graph has alot of edges
                O(V^2) is better than O((V + V^2) log V)

        Complexity for min-heap-based priority queue:
            Time: O((V + E) log V), where V is the number of vertices, E is the number of edges
            Space: O((V + E) log V)
            Note:
                This might be better than the array-based varient if the graph is sparse
'''

# Solution
import sys


class ShortestPathSolution:

    def __init__(self, graph):
        if graph is None:
            raise TypeError('graph cannot be None')
        self.graph = graph
        self.previous = {}  # Key: node key, val: prev node key, shortest path
        self.path_weight = {}  # Key: node key, val: weight, shortest path
        self.remaining = PriorityQueue()  # Queue of node key, path weight
        for key in self.graph.nodes.keys():
            # Set each node's previous node key to None
            # Set each node's shortest path weight to infinity
            # Add each node's shortest path weight to the priority queue
            self.previous[key] = None
            self.path_weight[key] = sys.maxsize
            self.remaining.insert(
                PriorityQueueNode(key, self.path_weight[key]))

    def find_shortest_path(self, start_node_key, end_node_key):
        if start_node_key is None or end_node_key is None:
            raise TypeError('Input node keys cannot be None')
        if (start_node_key not in self.graph.nodes or
                end_node_key not in self.graph.nodes):
            raise ValueError('Invalid start or end node key')
        # Set the start node's shortest path weight to 0
        # and update the value in the priority queue
        self.path_weight[start_node_key] = 0
        self.remaining.decrease_key(start_node_key, 0)
        while self.remaining:
            # Extract the min node (node with minimum path weight)
            # from the priority queue
            min_node_key = self.remaining.extract_min().obj
            min_node = self.graph.nodes[min_node_key]
            # Loop through each adjacent node in the min node
            for adj_key in min_node.adj_nodes.keys():
                # Node's path:
                # Adjacent node's edge weight + the min node's
                # shortest path weight
                new_weight = (min_node.adj_weights[adj_key] +
                    self.path_weight[min_node_key])
                # Only update if the newly calculated path is
                # less than the existing node's shortest path
                if self.path_weight[adj_key] > new_weight:
                    # Set the node's previous node key leading to the shortest path
                    # Update the adjacent node's shortest path and
                    # update the value in the priority queue
                    self.previous[adj_key] = min_node_key
                    self.path_weight[adj_key] = new_weight
                    self.remaining.decrease_key(adj_key, new_weight)
        # Walk backwards to determine the shortest path:
        # Start at the end node, walk the previous dict to get to the start node
        result = []
        current_node_key = end_node_key
        while current_node_key is not None:
            result.append(current_node_key)
            current_node_key = self.previous[current_node_key]
        # Reverse the list
        return result[::-1]
