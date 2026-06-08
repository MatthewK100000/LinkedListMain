from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        
        while (dummy.next is not None):
            while dummy.val == dummy.next.val:
                dummy.next = dummy.next.next # will output to None if tail
            
            if dummy.next is not None:
                dummy = dummy.next
            
        return head
    
arr = [1,1,2]

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
head = n1

# print(head.val)
# print(head.next.val)
# print(head.next.next.val)


s = Solution()
print(s.deleteDuplicates(head).val)

for i in range(0,len(arr)-1):
    node = ListNode(val = arr[i])
    if i == 0:
        head = node
    node.next = ListNode(val = arr[i+1])

node = ListNode(val = arr[0])
while node.next is not None:
    node.next = 

head_ = []
dummy_ = head
while dummy_.next is not None:
    head_.append(dummy_.val)
    dummy_ = dummy_.next
    print(dummy_.val)

print(head_)
    




