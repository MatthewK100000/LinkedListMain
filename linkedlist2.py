from linkedlistmain import SinglyLinkedList, Node

def SwapNodesInPairs(sll):
    head = sll.head
    dummy = head.next # new head will start at 2 
    sll.head = dummy

    prev = head
    curr = head.next
    nextnode = curr.next

    keep_iterating = True
    while keep_iterating:
        curr.next = prev
        prev.next = nextnode

        if nextnode is None:
            keep_iterating = False
            continue

        curr = nextnode
        nextnode = curr.next

        if nextnode is None:
            keep_iterating = False
            continue
        else:
            prev.next = nextnode
            prev = curr
            curr = nextnode
            nextnode = curr.next

    return sll

''' leetcode solution format

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None): # empty or 1 element edge case. Nothing more to do!
            return head

        dummy = head.next

        prev = head
        curr = head.next
        nextnode = curr.next

        keep_iterating = True
        while keep_iterating:
            curr.next = prev
            prev.next = nextnode

            if nextnode is None:
                keep_iterating = False
                continue

            curr = nextnode
            nextnode = curr.next

            if nextnode is None:
                keep_iterating = False
                continue
            else:
                prev.next = nextnode
                prev = curr
                curr = nextnode
                nextnode = curr.next
        return dummy 
        
'''
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    sll = SinglyLinkedList(arr)
    print(SwapNodesInPairs(sll))

