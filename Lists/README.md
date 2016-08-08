## List-based Collections

* This module covers the various list-based data structures commonly used in algorithms.
* Collection is a very basic concept is basically a collection of items that may or may not have shared properties.
* List: is a more specific data structure. In a list all the elements have shared properties and are related to each other.
* Array: is a specific implementation of a list. Each element of the list is characterized by an index. This makes insert and delete operations difficult i.e. O(n) time complexity.
* Linked list: is another implementation of a list. Each element is characterized by links to other items in the list. This makes insert and delete operations easy.
* Stack: Follows LIFO (Last In First Out) format similar to a stack of trays in the cafeteria. It has the pop and push functions to interact with the stack. It can be implemented using a linked list.
* Queue: Follows FIFO (First In First Out) format similar to the queue in the cafeteria. It has enque and deque functions to interact with the queue. It can be implemented using a linked list. There can also be double ended queues (deque) which work as both a stack and a queue.
* Priority Queue: is a special case of a queue where in each element also has a priority. Enque function remains the same, however the deque is modified to remove the element with the highest priority first. It can be like waiting in a hospital emergency room where patients are treated based on the severity of their condition.

### Practice Problems

* [linkedlist.py](linkedlist.py): Practice problem for implementing a linked list.
* [stack.py](stack.py): Practice problem for implementing a stack with linked list base.
* [queue.py](queue.py): Practice problem for implementing a queue with python list base.
