

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_link_from_list(values):
    head = ListNode(val=values[0])
    p = head
    # 逐个为 data 内的数据创建结点, 建立链表
    for i in values[1:]:
        node = ListNode(i)
        p.next = node
        p = p.next
    return head

