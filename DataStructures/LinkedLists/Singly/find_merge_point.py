"""
    Find the node at which both lists merge and return the data of that node.
    head could be None as well for empty list

    Input
        1
         \
          2 --> 3 --> None
         /
        1

        1 --> 2
               \
                3 --> None
               /
              1
    Output
        2
        3
"""
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Implement
def FindMergeNode(headA, headB):
    pass


# Solution
def FindMergeNodeSolution(headA, headB):
    if headA is None or headB is None:
        return None

    def _getTailAndSize(alist):
        if alist is None:
            return None
        size = 1
        while alist.next is not None:
            size += 1
            alist = alist.next
        return (alist, size)

    tailA, sizeA = _getTailAndSize(headA)
    tailB, sizeB = _getTailAndSize(headB)

    if tailA != tailB:
        return None

    if sizeA < sizeB:
        shorter, longer = headA, headB
    else:
        shorter, longer = headB, headA

    size_difference = abs(sizeA-sizeB)
    while size_difference > 0:
        longer = longer.next
        size_difference -= 1

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return shorter.data or longer.data
