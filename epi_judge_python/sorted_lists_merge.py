from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(list1: Optional[ListNode],
                           list2: Optional[ListNode]) -> Optional[ListNode]:
    curr1 = list1
    curr2 = list2
    res = ListNode()
    tail = res
    while curr1 and curr2:
        if curr1.data < curr2.data:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        
        tail = tail.next
    
    if curr1:
        while curr1:
            tail.next = curr1
            curr1, tail = curr1.next, tail.next      
    else:
        while curr2:
            tail.next = curr2
            curr2, tail = curr2.next, tail.next  
            
    return res.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
