#! /usr/env/bin python

import datetime

opss = ['-', '+', '/', '*']
opsss = set(opss)

# nums = [4, 1, 2, 10]
# desired_result = 11

# nums = [50, 100, 150, 8, 2, 50]
# desired_result = 570

# nums = [25, 50, 5, 7, 4, 4]
# desired_result = 641
# (25, 50, 5, 7, 4, 4) ('-', '-', '-', '*', '*') [25, 7, 4, '*', '*', 50, '-', 5, '-', 4, '-'] 641

# nums = [100, 6, 5, 100, 4, 4]
# desired_result = 743
# Started 2019-09-14 00:18:00.378074
# (100, 6, 5, 100, 4, 4) ('-', '-', '+', '+', '*') [100, 6, '+', 4, 4, '+', '*', 5, '-', 100, '-'] 743
# Finished 2019-09-14 00:23:04.951927

# nums = [9, 25, 5, 7, 3, 8]
# desired_result = 799
# Started 2019-09-14 13:50:18.229112
# (9, 25, 5, 7, 3, 8) ('-', '-', '-', '*', '*') [9, 25, 7, '-', 5, '*', '*', 3, '-', 8, '-'] 799
# Finished 2019-09-14 13:54:04.838940

# handle invalid calculations as divided by 0
def handle(f):
    def safe_f(*arg, **kw):
        try:
            return f(*arg, **kw)
        except:
            return 0
    return safe_f

ops = {
  "+": handle(lambda a, b: a + b),
  "-": handle(lambda a, b: a - b),
  "*": handle(lambda a, b: a * b),
  "/": handle(lambda a, b: a / b)
}

# remove num from list l without modifying orginal list
def remove(l, num):
    index = l.index(num)
    return l[:index] + l[index+1:]

# Generate a list of vertex that we can visit from current vertex
def get_next_values(vertex):
    current_number = vertex[0]
    nums = vertex[2]
    return [(ops[op](current_number, avail_number), str(avail_number) + " " + op, remove(nums, avail_number)) for op in ops for avail_number in nums]


def eval(tokens):
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()

# Simply do BFS on graph with start is 0 and end is our desired_result
def find_match(numbers, operations, desired_result):
    start = (0, "0", numbers)
    # Each vertex is in format (current value, "how to get to this value", available number that we can use to build next values)


    queue = [[start]]
    visited = []

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex[0] == desired_result:
            return " ".join(a[1] for a in path)
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in get_next_values(vertex):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.append(vertex)


if __name__ == '__main__':
    print('Started', datetime.datetime.now())
    exp = find_match(nums, opss, desired_result).split(' ')
    print(exp, eval(exp))
    print('Finished', datetime.datetime.now())
