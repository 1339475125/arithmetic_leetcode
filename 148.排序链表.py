#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        pre = ListNode(None)
        pre.next = head
        while pre.next:
            res.append(pre.next.val)
        res = self.mergeSort(res)
        return head

    def mergeSort(self, data):
        if len(data) < 2:
            return data
        size = len(data)
        mid = size / 2
        left = data[:data]
        right = data[mid+1:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, left, right):
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0));
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0));
        return result
        
# @lc code=end

