# https://leetcode.com/problems/reverse-linked-list-ii/description/
# tip 1: Look at solution if elegant, could give you that neat trick to make this code cleaner and more concise
# tip 2: Go through the edge cases one by one and tweak code as necessary
# tip 3: Practice and build muscle memory. Should do this in your sleep. 

from linkedlistmain import SinglyLinkedList, Node

def reverseBetween(ll, left, right):
    assert isinstance(ll, SinglyLinkedList)
    assert isinstance(left, int)
    assert isinstance(right, int)
    assert left <= right

    if left == right: # no reversals required
        return ll
    
    node = ll.head
    left_nonreversed_node = None
    left_reversed_node = None
    right_nonreversed_node = None
    right_reversed_node = None
    i = 1

    while i <= left - 1:
        if i == left - 1:
            left_nonreversed_node = node
        node = node.next
        i += 1
    
    # left_nonreversed_node.next = Node(9)
    # return ll

    nextnode = None
    while i + 1 <= right:
        # print(i)
        if i == left:
            left_reversed_node = node
        
        prev = node

        if nextnode is None:
            curr = node.next
        else:
            curr = nextnode

        if nextnode is None:
            nextnode = node.next.next if node.next is not None else None
        else:
            nextnode = nextnode.next

        curr.next = prev
        node = curr
        i += 1

        if i == right:
            print(1)
            right_reversed_node = curr
            right_nonreversed_node = nextnode

            if left_nonreversed_node is not None:
                left_nonreversed_node.next = right_reversed_node
            else:
                ll.head = right_reversed_node # move the head to beginning of reversed list since there is no left non reversed nodes

            if right_nonreversed_node is not None:
                left_reversed_node.next = right_nonreversed_node
            else:
                left_reversed_node.next = None

            return ll



if __name__ == '__main__':
    sll = SinglyLinkedList([i for i in range(1,1001)])
    left = 2
    right = 77
    print(reverseBetween(sll, left, right))








