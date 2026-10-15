# from functools import reduce

# my_list = [1, 2, 3]

# def mult_by_2(item):
#     return item * 2

# def is_odd(item):
#     return item % 2 != 0

# def accumulator(acc, item):
#     return acc + item

# print(reduce(accumulator, my_list, 0))

my_list = [1,2,3]
def mult_by_2(item):
    return item*2

def is_odd(item):
    return item % 2 != 0

def accumulator(acc , item):
    return acc + item

print(my_list)
print(list(filter(lambda item : item % 2 != 0, my_list)))