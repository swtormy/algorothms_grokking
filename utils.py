import math


def log_round(base: int, x: int) -> int:
    log_round = round(math.log(x, base))
    return log_round

def factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def sum_func(arr: list) -> int:
    if arr == []:
        return 0
    return arr[0] + sum_func(arr[1:])

def count_func(arr: list) -> int:
    if arr == []:
        return 0
    return 1 + count_func(arr[1:])

def max_func(arr: list) -> int:
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    max_sub = max_func(arr[1:])
    return arr[0] if arr[0] > max_sub else max_sub 
