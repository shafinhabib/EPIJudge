from typing import List

from test_framework import generic_test


def plus_one(l: List[int]) -> List[int]:
    i = -1
    while i >= -len(l) and l[i] == 9:
        l[i] = 0
        i -= 1
    if i == -len(l)-1:
        l.insert(0, 1)
    else:
        l[i] += 1
    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
