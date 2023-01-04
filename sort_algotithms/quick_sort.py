from random import randint
import sys

def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        index = round(len(arr) / 2) #randint(0, len(arr)-1)
        pivot = arr.pop(index) #arr[0]
        less = [i for i in arr if i < pivot]
        greather = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greather)


