from functools import reduce


def map_filter_demo(nums):
    squared = list(map(lambda x: x ** 2, nums))
    evens = list(filter(lambda x: x % 2 == 0, squared))
    return evens


def reduce_demo(nums):
    return reduce(lambda a, b: a + b, nums)


def compose(*funcs):
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed


def curry(fn):
    def curried(*args):
        if len(args) >= fn.__code__.co_argcount:
            return fn(*args)
        return lambda *more: curried(*args, *more)
    return curried


def pipe(*funcs):
    def piped(x):
        for f in funcs:
            x = f(x)
        return x
    return piped


def partition(pred, items):
    true_list = []
    false_list = []
    for item in items:
        if pred(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return true_list, false_list
