from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        n = i
        while perm[n] >= 0:
            A[i], A[perm[n]] = A[perm[n]], A[i]
            temp = perm[n]
            perm[n] -= len(perm)
            n = temp
    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
