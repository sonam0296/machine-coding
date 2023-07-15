import sys
from keyValue import HashMap

sys.path.append('/Users/sonamjha/sonam_project/python_projects/machine_coding')

# Create instance of hashmap
hashMap = HashMap()

# Set key-value pair for hashMap
hashMap.set('key1', 'value1')
hashMap.set('key2', 'value2')

# Retrieve value
print(hashMap.get('key1'))
print(hashMap.get('key2'))

#Check if key already exists
print(hashMap.contains('key1'))

#Delete key valye pair
hashMap.delete('key1')

print(hashMap.contains('key1'))
print(hashMap.get('key1'))