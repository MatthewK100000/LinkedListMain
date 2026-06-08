class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class SinglyLinkedList:
	def __init__(self, nodes = None):
		self.head = None
		if nodes is not None:
			node = Node(val = nodes.pop(0))
			self.head = node
			for elem in nodes:
				node.next = Node(val = elem)
				node = node.next

	def __repr__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(str(node.val))
			node = node.next

		nodes.append("None")
		return " -> ".join(nodes)

	# previous node is at position i-1
	def add_node(self, prev_node, node_to_add):
		assert isinstance(prev_node, Node)
		assert isinstance(node_to_add, Node)
	
		curr_node = prev_node.next # because you can only go forward in a singly-linked list, you need to pass prev_node as an arg and from there you can get curr_node
		node_to_add.next = curr_node
		prev_node.next = node_to_add
		return

	def delete_node(self, prev_node):
		assert isinstance(prev_node, Node)
		curr_node = prev_node.next.next
		prev_node.next = curr_node

	def delete_node_at_end(self):
		node = self.head
		while node is not None:
			if node.next.next is None:
				final_node = node
				final_node.next = None
				node = None
			else:
				node = node.next
		return

	def delete_node_at_start(self):
		self.head = self.head.next
		return

	def reverse(self):
		prev = None
		curr = self.head
		while curr is not None:
			if curr.next is None:
				self.head = curr
			next_node = curr.next # don't lose track of next node and all nodes after

			curr.next = prev # reverse direction of pointer

			# move on to the next pair of nodes
			prev = curr
			curr = next_node

		return

if __name__ == '__main__':
	arr = [1,2,3,4,5]
	ll = SinglyLinkedList(arr)

	print('current: ', ll)
	print('current head: ', ll.head.val)
	
	# reverse the linked list
	ll.reverse()
	print('reversed: ', ll)
	print('reversed head: ', ll.head.val)

	# reverse linked list again
	ll.reverse()
	print('current (reversed again): ', ll)
	print('current head (reversed again): ', ll.head.val)

	# remove the third node
	second_node = ll.head.next
	third_node = second_node.next
	print('third node val: ', third_node.val)
	ll.delete_node(second_node)
	print('third node deleted: ', ll)

	# remove node from start
	ll.delete_node_at_start()
	print('first node deleted (head changed): ', ll)
	
	# remove node at the end
	ll.delete_node_at_end()
	print('last node deleted (in O(n) time, would be O(1) if array)', ll)
	
	# add a node in the middle
	node_two = ll.head
	ll.add_node(prev_node = node_two, node_to_add = Node(val = 6))
	print(ll)
	
	# add a node at the end
	node_four = ll.head.next.next
	ll.add_node(prev_node = node_four, node_to_add = Node(val = 7))
	print(ll)