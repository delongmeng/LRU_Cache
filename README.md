# LRU_Cache


Problem:

Least Recently Used Cache

The goal will be to design a data structure known as a Least Recently Used (LRU) cache. 
An LRU cache is a type of cache in which we remove the least recently used entry when 
the cache memory reaches its limit. For the current problem, consider both get and set 
operations as an use operation.


My code analysis:

To achieve the goal of O(1) time complexity for all operations, including get() and set(), I use a dictionary as the main data structure to store the cache, so that I can look up the key value in constant time. 

However, get() is also a 'use' operation, because I need to reset the location of the data after I visit it. To do that, I store the data in the form of 'node' as the value of the dictionary. Thus, given any key, I can immediately visit the corresponding node through the dictionary. 

All of the nodes are linked together to form a doubly linked list. Each node has a previous node and a next node. At the two ends, I put a permanent 'head' node and a permanent 'tail' node, which are also stored in the initial dictionary. These two nodes will always be there and indicate the entrance and exit of the list. 

Tho whole linked list can also be considered as a queue. New cache comes in from the head (entrance), and oldest cache will be pushed out from the tail (exit) when the queue is full. The only difference from a traditional queue is that when a node is visited, it can be easily pulled back to the front (head). 

Another point is that when a node is deleted, the corresponding dictionary record need also be deleted, so the key of each cache is not only in the 'key' of the dictionary, but is also copied in the 'value' of the node using a tuple of (key,value). Thus, the dictionary can point to the node, and the node can also direct back to the dictionary. 

In summary, through this dictionary-doubly linked list (queue) structure, we can perform all of the cache operation in constant time (O(1)). The time complexity is O(1) for each operation. 
