from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def arr_to_list_node(arr: List[int]) -> ListNode:
    current = None
    next = None
    for x in reversed(arr):
        current = ListNode(x, next=next)
        next = current
    return current


def node_to_int(node: ListNode) -> int:
    if node.next is None:
        return node.val

    next = node_to_int(node.next) * 10
    value = node.val
    return value + next


def int_to_node(num: int) -> ListNode:
    s = reversed(str(num))
    return arr_to_list_node([int(x) for x in s])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # This works because Python 3 uses long ints, which are limited only by
        # memory: https://www.python.org/dev/peps/pep-0237/
        l1_int = node_to_int(l1)
        l2_int = node_to_int(l2)
        sum = l1_int + l2_int
        return int_to_node(sum)


if __name__ == '__main__':
    s = Solution()

    for l1, l2, exp, name in [
        (
            [2, 4, 3],
            [5, 6, 4],
            [7, 0, 8],
            "case 1",
        ),
        (
            [0],
            [0],
            [0],
            "case 2",
        ),
        (
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
            "case 3",
        ),
    ]:
        res = s.addTwoNumbers(arr_to_list_node(l1), arr_to_list_node(l2))
        if node_to_int(res) != node_to_int(arr_to_list_node(exp)):
            print(f"{name}, exp: {exp}, res: {res}")
        else:
            print(f"passed: {name}")
