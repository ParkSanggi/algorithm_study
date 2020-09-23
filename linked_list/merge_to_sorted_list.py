
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_two_list(l1, l2)
    return l1


