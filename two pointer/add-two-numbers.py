class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_start =currt= ListNode()
        val= tens = 0 
        while l1 is not None or l2 is not None or tens:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + tens
            unit, tens = val % 10, val // 10
            print(unit,tens)
            currt.next = ListNode(unit)
            currt = currt.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return pre_start.next


def create_list(listt):
    start = ListNode(-1)
    curt = start
    for i in range(len(listt)):
        curt.val = listt[i]
        curt.next = ListNode(-1) if i != len(listt) - 1 else None
        curt = curt.next
    return start


def print_list(listnode):
    res = []
    while listnode is not None:
        res.append(listnode.val)
        listnode = listnode.next
    print(res)


solution = Solution()
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
l1 = create_list(l1)
l2 = create_list(l2)
result = solution.addTwoNumbers(l1, l2)
# print(result.next.val)
print_list(result)
