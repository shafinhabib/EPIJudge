from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, s: int,
                    f: int) -> Optional[ListNode]:
    w = []
    if L is None or L.next is None:
        return L

    l = ListNode(0, L)
    ptr = l
    c = 0
   
    for i in range(1,s):
        ptr = ptr.next

    curr = ptr.next
    for i in range(f-s):
        temp = curr.next
        curr.next = temp.next
        temp.next = ptr.next
        ptr.next = temp
    return l.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
