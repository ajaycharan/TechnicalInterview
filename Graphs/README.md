## Graphs

* Graph is a data structure where the nodes have some relationships among themselves. Graph is a more generic instance of tree which can be disconnected and also have cycles. The edges can also have values representing the strength of relationships between nodes. These graphs can be used to store any sort of semantic data.
* Directed Graph is an instance wherein the edges have directions. This will lead to start and end nodes.
* Cycles in a graph can be dangerous as it could lead to infinite loops in a programmatic implementation. A special type of DG is an acyclic directed graph.
* Connectivity is a metric used to measure the strength of a graph.
* Graphs can be efficiently represented using various representations such as Edge lists, adjacency lists and an adjacency matrix. These representations can be used in various implementations depending on the use case.
* Graph traversal: is similar to tree traversal. The two approaches are DFS and BFS. The traversal algorithms have time complexity of O(|E|+|V|) i.e. it depends on the number of nodes and edges.
* DFS is implemented using a list of seen nodes implemented as a stack. BFS implements the list of seen nodes as a queue. These traversals are basically building a tree from the graph.
* There several useful paths for a graph. A eulerian path traverses every edge and finishes at the same start node. A graph can be considered eulerian if the graph is connected and all the nodes have degree of 2. There are also other notable paths such as an Hamiltonian path.

### Practice Problems

* [graphrepresentation.py](graphrepresentation.py): Implementations to generate edge list, adjacency list and adjacency matrix from a graph.
* [graphtraversal.py](graphtraversal.py): Implementation of BFS traversal of a graph.
