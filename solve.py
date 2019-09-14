#! /usr/env/bin python

from itertools import permutations, combinations_with_replacement
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


ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b)
}

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

def valid(exp):
    nums = 0
    ops = 0
    for e in exp:
        if e in opsss:
            ops += 1
        else:
            nums += 1
        if ops >= nums:
            return False
    return True

def find_match(numbers, operations):
    for p in permutations(numbers):
        for o in combinations_with_replacement(operations, len(numbers)-1):
            rs = p + o

            for r in permutations(rs):
                s = list(r)
                if valid(s):
                    try:
                        val = eval(s)
                        if val == desired_result:
                            print(p, o, s, val)
                            return
                    except:
                        pass

if __name__ == '__main__':
    print('Started', datetime.datetime.now())
    find_match(nums, opss)
    print('Finished', datetime.datetime.now())
