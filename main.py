from search_algorithms.binary_search import binary_search
from sort_algotithms.simple_sort import selection_sort
from sort_algotithms.quick_sort import quick_sort
from utils import log_round
from random import randint


my_list = list(range(100))
random_arr = list(range(6, 11)) + list(range(1, 6))

# #logarithm
# print(log_round(2, 1024))
# #binary_search
# print(binary_search(my_list, 2))
# #simple_sort

# print(selection_sort(random_arr))
#quicksort
print(quick_sort(random_arr))