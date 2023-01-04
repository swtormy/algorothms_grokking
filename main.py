from search_algorithms.binary_search import binary_search
from sort_algotithms.sorting_by_selection import selection_sort
from sort_algotithms.quick_sort import quick_sort
from utils import log_round
from random import randint
from time import time
import sys


print('Recursions before:', sys.getrecursionlimit())
sys.setrecursionlimit(15000)
print('Recursions after:', sys.getrecursionlimit())

my_list = list(range(100))
random_arr = list(range(6, 11)) + list(range(1, 6))

# #logarithm
# print(log_round(2, 1024))
# #binary_search
# print(binary_search(my_list, 2))

# #simple_sort
# start = time()
# print(selection_sort(random_arr))
# end = time() - start
# print('Simple sort:', end)
#quicksort
start = time()
print(quick_sort(random_arr))
end = time() - start
print('Quick sort:', end)
