class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		new_node = Node(key)
		new_node.next = self.head
		self.head = new_node
		self.size += 1


	def pushBack(self, key):#tail 뒤에 노드 추가
		new_node = Node(key)
		if self.size == 0: #비어 있다면 새로 들어오는게 head가 된다
			self.head = new_node
		else:
			tail = self.head
			while tail.next != None:
				tail = tail.next
			tail.next = new_node
		self.size += 1

	def popFront(self): 
		# head 노드의 값 리턴. empty list이면 None 리턴
		key = None #주의
		if len(self) > 0:
			key = self.head.key
			self.head = self.head.next
			self.size -= 1
		return key

	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if self.size == 0:
			return None
		else:
			#tail 노드와 그 전 노드인 previous를 찾는다
			previous, current = None, self.head
			while current.next != None:
				previous, current = current, current.next # 한 노드씩 진행
			#만약 리스트에 노드가 하나면 그 노드가 head이면서 tail
			#이런 경우 tail을 지우면 빈 리스트가 되므로 head = None으로 수정해야함
			tail = current
			key = tail.key
			if self.head == tail:
				self.head = None
			else:
				previous.next = tail.next
			self.size -= 1
			return key

	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head
		while v:
			if v.key == key:
				return v
			v = v.next
		return None
		
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		if x == None:#빈리스트라는 의미
			return False
		elif x == self.head: #head가 삭제해야할 노드인경우
			self.popFront()
			return True
		else:#빈리스트도 아니고, 삭제해야할 x가 head도 아닌 경우
			previous, current = None, self.head
			while current.next != x.next:
				previous,current = current, current.next
			previous.next = current.next
			self.size -= 1
			return True

	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")
