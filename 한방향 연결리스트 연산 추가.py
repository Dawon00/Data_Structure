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
	
	def __len__(self):#self의 size를 리턴한다
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):#key값 가지는 노드를 만들어 맨앞에 삽입
		new_node = Node(key)#key값 가지는 new_node를 만든다
		new_node.next = self.head#new_node의 다음이 head가 된다
		self.head = new_node#self의 head는 new_node가 된다
		self.size += 1#size를 하나 증가시킨다
		
	def pushBack(self, key):#tail 뒤에 노드를 만들어 삽입
		new_node = Node(key)#key값 가지는 new_node를 만든다
		if self.size == 0: #비어 있다면 새로 들어오는게 head가 된다
			self.head = new_node
		else:
			tail = self.head#tail은 head부터 시작한다
			while tail.next != None:#한바퀴를 돈다
				tail = tail.next#tail을 한칸 이동한다
			tail.next = new_node#tail의 다음에 new_node를 넣는다
		self.size += 1#size를 하나 증가시킨다
		
	def popFront(self): 
		# head 노드의 값 리턴. empty list이면 None 리턴
		headkey = None #key의 초기값은 None
		if len(self) > 0:#빈리스트가 아니라면
			headkey = self.head.key#headkey에 head의 key를 넣어준다
			self.head = self.head.next#head 다음에 있던걸 head라고 지정한다
			self.size -= 1#size를 하나 줄인다
		return headkey#head 노드값을 리턴한다
	
	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if self.size == 0:#빈리스트이면 None을 리턴한다
			return None
		else:
			#tail 노드와 그 전 노드인 previous를 찾는다
			previous = None#previous 초기값은 None
			current = self.head#current는 head부터 시작한다
			while current.next != None:#한바퀴를 돈다
				previous = current # 한 노드씩 진행
				current = current.next#한칸 옆으로 이동한다
			tail = current#current를 tail에 넣는다
			key = tail.key#tail의 key를 key에 담는다
			if self.head == tail:#tail이랑 head가 같으면 그 노드가 head이면서 tail
				self.head = None#이런 경우 tail을 지우면 빈 리스트가 되므로 head = None으로 수정해야함
			else:#그런 경우가 아니라면 tail.next값을 previous.next랑 연결한다
				previous.next = tail.next
			self.size -= 1#self의 size를 하나 줄인다
			return key#tail의 key를 리턴한다
		
	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head#v는 head부터 시작
		while v:#한바퀴를 돈다
			if v.key == key:#key와 같은 값을 찾으면 v를 리턴한다
				return v
			v = v.next#한칸 옆으로 이동한다
		return None
	
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		if x == None:
			return False
		elif x == self.head: #head가 삭제해야할 노드인경우
			self.popFront()#head를 지워주는 popFront를 불러온다
			return True
		else:# 위의 경우에 해당이 안된다면(head, None이 아닌 노드를 지우고자 함)
			previous, current = None, self.head#previous와 current는 각각 None, head에서 시작
			while current.next != x.next:#x.next와 current.next가 같아지면 반복문을 빠져나올것이다
				previous,current = current, current.next#previous와 current를 한칸씩 옆으로 이동
			previous.next = current.next#previous의 다음 노드를 가리키는 링크가 current의 다음것을 가리키도록 함.
			self.size -= 1#size를 하나 줄인다
			return True
		
	def reverse(self, key):#key값을 갖는 노드부터 tail 노드까지의 노드들을 반대로 뒤집는다
		if self.search(key) == None:#빈리스트라면 None을 리턴한다
			return None
		p = self.search(key)#key를 갖는 노드를 p에 넣는다
		q = None#q와 r의 초기값은 None이다
		r = None
		s = self.head#s는 head에서 시작한다
		while p != None:#p부터 끝까지 돈다
			r = q#변수들을 옆으로 이동해가면서 링크들을 뒤집는다(이전것을 가리키도록)
			q = p
			p = p.next
			q.next = r
		if key !=  self.head.key: #처음부터 뒤집는게 아니라면
			while s.next != self.search(key):#s.next가 입력한 key값을 갖는 노드와 같으면 반복문을 빠져나온다 
				if s.next == None:#s다음에 None이면 반복문을 빠져나온다
					break
				else:#그게 아니라면 s를 한칸옆으로 이동한다
					s = s.next
			s.next = q#s의 next는 q가 된다
		else:#처음부터 전체를 다 뒤집는 경우엔 head부터 뒤집는다
			self.head.next = None
			self.head = q#head는 q가 된다
	
	def findMax(self):#최대 값을 찾는 함수
		# self가 empty이면 None, 아니면 max key 리턴
		if self.size == 0:#빈리스트인경우
			return None
		else:#빈리스트가 아닌경우
			current = self.head#current는 head부터 시작
			maxkey = self.head.key#maxkey는 처음엔 head의 key부터 시작
			while(current != None):#살펴보는 key가 None이기 전까지 반복
				if(maxkey < current.key):#만약 maxkey가 current보다 작다면
					maxkey = current.key#maxkey 업데이트
				current = current.next#current 한칸 옮기기
		return maxkey#maxkey 리턴하기
	
	def deleteMax(self):
		# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		current = self.head
		if self.size == 0:#빈리스트 인경우 None리턴
			return None
		else:
			maxkey = self.findMax()#maxkey에 최대 값을 담는다
			maxnode = self.search(maxkey)#maxnode를 찾는다
			self.remove(maxnode)#maxnode 를 remove 한다
			return maxkey
	
	
	def insert(self, k, val):#k번째 노드 다음에 key를 새로 추가하는 함수
		if k > self.size:#노드 개수가 k보다 작으면 가장 뒤에 삽입하기로 한다
			self.pushBack(val)#가장 뒤에 삽입할 땐 기존에 만들어놓은 pushBack함수를 이용
		else: #head 노드로 부터 k번째에 있는 노드 다음에 삽입한다.
			new_node = Node(val)#val을 갖는 new_node를 만들어준다
			index = 1#index는 1부터 시작한다
			cur = self.head#cur는 head부터 시작한다
			while True:
				if index == k:#만약에 index가 k번째가 되었으면 그땐 반복문을 빠져나온다
					break
				cur = cur.next#cur를 한칸 옆으로 이동한다
				index += 1#index도 하나 증가시킨다
			#cur에 들어있는게 k번째 노드
			cur_next = cur.next#cur의 다음에 있는걸 cur_next라고 한다
			cur.next = new_node#cur의 다음에 new_node가 오도록한다
			new_node.next = cur_next#new_node의 다음에는 cur_next가 오도록한다
			self.size += 1#size를 하나 증가시킨다
			
		
	def size(self):#size를 리턴하는 함수
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
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
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
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")
