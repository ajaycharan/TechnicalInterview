## Trees

* Tree can be considered as an extension to a linked list. It is also a specific instance of a graph that is connected and does not have any cycles. The first node of a tree is called the root node.
* There are various terms used with respect to trees. It has levels where the root node is of level 1. Nodes have parent-child relationships and nodes with children are called leaf nodes. Height and depth are two parameters to describe a tree. Height is from the root node to the leaf and depth is the inverse.
* Traversal of a tree can be a challenging problem. There are several approaches: Depth First Search (DFS), Breadth First Search (BFS) also called Level order traversal.
* Within DFS, there are several approaches of traversing the tree, i.e. Preorder, Inorder and Postorder.
* Searching and Deleting of elements in a tree have O(n) time complexity as we might have to traverse through the whole tree. However, an insert operation only depends on the height of the tree which reduces time complexity to O(logn).
* Rules can be applied to the ordering of nodes in a tree to make it application specific.
* Binary Search Tree: is a specific case, used for systemic handling of data. BST has search, insert and delete operations with average time complexity O(logn).
* However, we can obtain a highly unbalanced BST that can make the complexity O(n).
* Another implementation of a tree is the heap. Heap has the max or min element as the root. They can be implemented as binary trees or not leading to varying complexities. Searching for max element is O(1) and searching in general becomes O(n).
* Insert element is called an heapify operation as it leads to a reordering of the heap to ensure max/min element is at the top. Extract operation results in returning the root of a heap, after which a terminal node is placed as the heap and a heapify operation is performed.
* Heap can be implemented as an array where all the operations are performed by index in the array.
* Self Balancing Tree: Ensures that the tree is balanced. Red Black Tree is a special type where each node is either labeled as red or black. The labeling rules are such that the tree will become balanced. This makes sure that all operations are reduced to O(logn).

### Practice Problems

* [binarytree.py](binarytree.py): Implementation of traversal and searching in a binary tree.
* [binarysearchtree.py](binarysearchtree.py): Implementation of binary search tree, specifically insert and search operations.
