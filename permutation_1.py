from copy import deepcopy
from collections import Counter
from math import factorial

string = 'abcd'
def permutations(string):
    memory_set = {string}
    memory_list_for = [string]
    i = 0

    def enumeration(count_i, member):
        count_1 = 0
        work_list = list(member)
        while count_1 < len(member) - count_i:
            work_list.append(work_list.pop(count_i)) 
            memory_list.append(''.join(work_list))
            print('\nmemory_list', memory_list, '\nwork_list', work_list, '\n')
            count_1 += 1

    def pre_enumeration(memory_list):
        nonlocal i, memory_set, memory_list_for
        print('Что перебираем', memory_list_for)
        for perm_member in memory_list_for:
            print('Элементы перебора', perm_member)
            enumeration(i, perm_member)
            print('finish enumeration of one member\ni', i, '\nmemory_list', memory_list)
        memory_set = memory_set.union(set(memory_list))
        memory_list_for = deepcopy(memory_list)
        print('\nmemory_set', memory_set)
        i += 1

    def is_repeat():
        d = 1
        counter = Counter(string)
        for i in counter.values():
            d *= factorial(i)
        return int(factorial(len(string)) / d)

    number_perm = is_repeat()
    # k = 0
    # while k < 3:
    while len(memory_set) < number_perm:
        memory_list = []
        pre_enumeration(memory_list)
        # k += 1

    return print(memory_set)

permutations(string)

        
        

