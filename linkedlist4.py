# https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=linked-list

from linkedlistmain import SinglyLinkedList, Node

def mergeTwoLists(sll1,sll2):
    assert isinstance(sll1, SinglyLinkedList)
    assert isinstance(sll2, SinglyLinkedList)

    node1 = sll1.head
    node2 = sll2.head

    which_sll = None
    if node1.val <= node2.val:
        current_node = node1
        other_node = node2
        which_sll = 1
    else:
        current_node = node2
        other_node = node1
        which_sll = 2

    next_node = None
    while (other_node is not None):
        if (current_node.next is not None) and (current_node.next.val <= other_node.val):
            current_node = current_node.next
        else:
            next_node = current_node.next
            current_node.next = other_node
            current_node = other_node
            other_node = next_node
    
    result_sll = sll1 if which_sll == 1 else sll2
    return result_sll

if __name__ == '__main__':
    sll1 = SinglyLinkedList([1,2,8,8,9,11,12,13])
    sll2 = SinglyLinkedList([3,4,5,6,10,12])
    print(sll1)
    print(sll2)
    print(mergeTwoLists(sll1,sll2))

