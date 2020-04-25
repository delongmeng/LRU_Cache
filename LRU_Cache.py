

class CacheDoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LRUCache(object):

 
    def __init__(self, capacity):
        # Initialize class variables
        self.dict = {'head': CacheDoubleNode('head'), 'tail': CacheDoubleNode('tail')}
        self.dict['head'].next = self.dict['tail']
        self.dict['tail'].previous = self.dict['head']
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        # if hit, return the value
        # if miss, return -1
        if key not in self.dict:
            return -1
        
        else:
            # if hit, first get the value
            hit_node = self.dict[key]
            value = hit_node.value[1]
            
            # check if it's already at the front
            if hit_node.previous != self.dict['head']:
                # first release it from current location
                hit_node.previous.next = hit_node.next
                hit_node.next.previous = hit_node.previous  
                
                # then move the node to the front
                self.insert_front(hit_node)
            
            return value
            

    def put(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        if key in self.dict: # if key already exists, then just update the value
            self.dict[key].value = (key,value)

            # check if it's already at the front
            hit_node = self.dict[key]
            if hit_node.previous != self.dict['head']:
                # first release it from current location
                hit_node.previous.next = hit_node.next
                hit_node.next.previous = hit_node.previous  
                
                # then move the node to the front
                self.insert_front(hit_node)        
        
        else:
            if len(self.dict)-2 == self.capacity: # check if the cache is full
                # remove the oldest element first
                last_node = self.dict['tail'].previous
                self.remove_LRU(last_node)
    
            self.dict[key] = CacheDoubleNode((key,value))
            new_node = self.dict[key]
            self.insert_front(new_node)
        
    def remove_LRU(self, last_node):
        last_node.previous.next = last_node.next
        last_node.next.previous = last_node.previous
        last_node.previous = None
        last_node.next = None
        last_node_key = last_node.value[0]
        del self.dict[last_node_key]        
        
    def insert_front(self,new_node): # to insert a node to right after the 'head'
        new_node.next = self.dict['head'].next
        new_node.previous = self.dict['head']
        self.dict['head'].next.previous = new_node
        self.dict['head'].next = new_node        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Example:

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)     # returns 1
cache.put(3, 3)   # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)   # evicts key 1
cache.get(1)      # returns -1 (not found)
cache.get(3)      # returns 3
cache.get(4)      # returns 4


cache = LRUCache(2)

cache.get(2)     # returns -1
cache.put(2, 6)
cache.get(1)     # returns -1
cache.put(1, 5)  
cache.put(1, 2)   
cache.get(1)      # returns 2
cache.get(2)      # returns 6

