import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

class Node:
	def __init__(self, data):
		self.prev = None
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
		
	def append(self, data):
		new_node = Node(data)
		# 기존 요소가 0개인 경우
		if self.head is None:
			self.head = new_node
			self.head.prev = self.head
			self.head.next = self.head
		# 기존 요소가 1개 이상인 경우
		else:
			tail = self.head.prev
			
			tail.next = new_node
			new_node.prev = tail
			
			new_node.next = self.head
			self.head.prev = new_node
	
	def josephus(self, k):
		result = []
		current = self.head
		while current.next != current:
			for _ in range(k-1):
				current = current.next
			
			result.append(str(current.data))
			
			current.prev.next = current.next
			current.next.prev = current.prev
			current = current.next
			
		result.append(str(current.data))
		return result	
			
cll = CircularLinkedList()
for i in range(1, n+1):
	cll.append(i)

print("<", end = "")
print(", ".join(cll.josephus(k)), end = "")
print(">")
			
	
