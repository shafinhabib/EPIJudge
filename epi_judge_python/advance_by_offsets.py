from typing import List

from test_framework import generic_test


def can_reach_end(arr: List[int]) -> bool:
    idx, idx2 = 0, 0
    m_score = idx + arr[idx]
    p_score = 0

    while m_score < len(arr)-1:
        idx2, p_score = 0, 0
        for i in range(1, arr[idx]+1):
            if m_score <= arr[idx+i]+i+idx:
                if p_score <= arr[idx+i]+i+idx:
                    p_score = arr[idx+i]+i+idx
                    idx2 = idx+i
        if idx2 == 0:
            return False
        else:
            idx = idx2
            m_score = p_score
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
