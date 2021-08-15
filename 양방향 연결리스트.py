class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
	def splice(self,a,b,x):#a--b노드를 잘라서 x 뒤에 붙이는 함수
		if a == None or b == None or x == None:
			return
		a.prev.next = b.next#a의 전 노드와 b의 다음 노드를 연결함(자르기)
		b.next.prev = a.prev
		
		x.next.prev = b#x뒤에 a--b를 붙이기
		b.next = x.next
		a.prev = x
		x.next = a
		
	def moveAfter(self,a,x):#a를 x 뒤로 이동
		return self.splice(a,a,x)
	
	def moveBefore(self,a,x): #a를 x 앞으로 이동
		return self.splice(a,a,x.prev)
	
	def insertAfter(self,a,key):#key 값 가지는 노드를 a 뒤에 삽입
		b = Node(key) #key값을 가진 새로운 노드 b 만들기
		self.moveAfter(b,a)
		
	def insertBefore(self,a,key):#key값 가지는 노드를 a 앞에 삽입
		b = Node(key)#key값을 가지는 새로운 노드 b 만들기
		self.moveBefore(b,a)
		
	def pushFront(self,key):#key값 가지는 노드를 만들어 맨 앞에 삽입(head 노드 다음에)
		self.insertAfter(self.head,key)
		
	def pushBack(self, key):#key값 가지는 노드 만들어 맨 뒤에 삽입(head 노드 앞에)
		self.insertBefore(self.head, key)
		
	def deleteNode(self, x):#x노드를 삭제함(리스트에서 분리하기)
		x.prev.next = x.next
		x.next.prev = x.prev
		del x
		
	def popFront(self):#리스트의 가장 앞 노드key를 리턴하고 해당 노드를 deleteNode를 이용해 제거
		if self.head.next == self.head:#빈리스트이면 None리턴
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)#head 뒤에 있는 노드를 제거
		return key
	
	def popBack(self):#리스트의 가장 뒤 노드key를 리턴하고 해당 노드를 deleteNode를 이용해 제거
		if self.head.next == self.head:#빈리스트이면 None을 리턴
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)#head 앞에 있는노드를 제거
		return key
	
	def search(self, key):#key를 입력받아 노드를 찾아줌
		v = self.head.next#v는 head 노드다음에 있는 것부터 시작
		while v != self.head:#한바퀴를 다 돌기 전까지
			if v.key == key:#key와 같은 값을 찾으면
				return v#그 v를 리턴함
			v = v.next#찾지못하면 다음 노드로 넘어감
		return None

	def first(self):#맨 앞에있는 노드(head 다음에 있는 노드) 리턴
		if self.head.next == self.head:#빈리스트면 None 리턴
			return None
		return self.head.next
	
	def last(self):#맨 뒤에있는 노드(head 이전에 있는 노드) 리턴
		if self.head == self.head.next:#빈리스트면 None 리턴
			return None
		return self.head.prev
	
	def isEmpty(self):#리스트가 비어있는지 확인하는 함수
		if self.head == self.head.next:#비어있으면 True 리턴
			return True
		else:#아니라면 False 리턴
			return False
		
	def findMax(self):#빈리스트면 None, 아니면 최대 key값을 리턴한다	
		if self.isEmpty() == True:
			return None
		else:
			current = self.head.next#current는 맨 앞노드부터 시작한다
			maxkey = self.head.next.key#maxkey에는 최대값 key를 저장한다
			while(current.key != None):#한바퀴를 돌면서 max를 찾는다
				if(maxkey < current.key):#만약에 기존 maxkey보다 더 큰 값을 찾으면
					maxkey = current.key#maxkey를 업데이트 해준다
				current = current.next#다음 노드로 이동한다
			return maxkey#마지막에 maxkey를 반환한다
	
	def deleteMax(self):#최대 key값을 삭제하고 최대값을 리턴한다. 빈 리스트면 None을 리턴한다.
		if self.isEmpty() == True:
			return None
		else:
			maxkey = self.findMax()#maxkey에 최대값을 저장한다
			maxnode = self.search(maxkey)#maxnode를 search로 찾는다
			self.deleteNode(maxnode)#노드를 삭제해준다
			return maxkey #최대값 리턴
		
	def sort(self):#오름차순으로 리스트를 정렬하는 함수
		temp = []#값들을 담아둘 리스트를 만들어둔다
		while True:#self에서 최대값을 찾아 deleteMax하고 그값을 차례대로 temp에 쌓는다
			if self.head == self.head.next:
				break
			temp.append(self.deleteMax())
		temp.reverse()#temp를 뒤집어준다
		while True:#temp에서 마지막 값을 꺼내주는 동시에 self의 맨 앞에 넣어준다
			if len(temp) ==0:
				break
			self.pushFront(temp.pop())
		return self#정렬된 self를 리턴한다
  
  
L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")
