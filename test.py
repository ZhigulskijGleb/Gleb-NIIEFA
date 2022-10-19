string = 'abcd'
memory_set = {string}
memory_list = ['abcd', 'bcda', 'cdab', 'dabc']
memory_set = memory_set.union(set(memory_list))
print(memory_set)