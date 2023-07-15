class Node:  # stores key-value pair 
    def __init__(self, key, value) :
        self.key = key
        self.value = value
        self.next = None

class HashMap:  # stores actual hashmap
    def __init__(self, size=100):
        self.size = size
        self.buckets = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = Node(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    current.next = Node(key, value)
                    return
                current = current.next

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key): # Removes a key-value pair from the hashmap based on the given key.
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                return 
            prev = current
            current = current.next 

    def contains(self, key):  #Checks if a key is present in the hashmap.
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False
    

