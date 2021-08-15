class AdaptedHeap: # min_heap으로 정의함!
	def __init__(self):
		self.A = []
		self.D = {}  # dictionary D[key] = index

	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)

	def insert(self, key):
		# code here
		# key 값이 최종 저장된 index를 리턴한다!
		self.A.append(key) #A리스트에 key를 append하고 key에 따른 index도 D에 추가해준다
		self.D[key] = len(self.A) - 1
		self.heapify_up(len(self.A)-1) #방금 append한것을 heapify_up
		return self.D[key] #저장된 index를 리턴한다

	def heapify_up(self, k): #k는 index번호
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		while k > 0 and self.A[(k-1)//2] > self.A[k]: # 아직 root node에 도달하지 못했고, parent가 자기보다 크면
			temp = self.A[k] #parent와 자리를 바꿔준다(parent노드로 올라간다)
			self.D[self.A[k]] = (k-1)//2 #D에 저장된 값(index)을 모두 서로 바꿔준다
			self.D[self.A[(k-1)//2]] = k
			
			self.A[k] = self.A[(k-1)//2] #A리스트에 저장된 값도 서로 바꿔준다
			self.A[(k-1)//2] = temp
			k = (k-1) // 2

	
	def heapify_down(self, k): #k는 index
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		while 2 * k + 1 < self.__len__(): # 리프노트가 아니라면 내려가기
			L = 2 * k + 1 #L은 왼쪽 자식노드, R은 오른쪽 자식노드
			R = 2 * k + 2
			if L < self.__len__() and self.A[L] < self.A[k]: #왼쪽 자식노드가 더 작다면
				m = L #최소값 m은 L로 업데이트
			else: #현재 값이 더 작다면 m은 현재값
				m = k
			if R < self.__len__() and self.A[R] < self.A[m]: #오른쪽 자식노드가 더 작다면
				m = R #최소값 m은 R로 업데이트
				#m은 이제 A[k], A[R], A[L] 중 최소값의 인덱스
			if m != k: #A[k]가 최소값이 아니라면 min_heap성질에 위배
				temp = self.A[k] #k와 m의 자리를 바꿔준다
				temp1 = self.A[m]
				self.A[k] = self.A[m]
				self.A[m] = temp
				
				self.D[temp] = m #key값의 index도 서로 변경해줌
				self.D[temp1] = k
				k = m
			else: #A[k]가 최소값이라면 반복문을 빠져나온다
				break

	def find_min(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 리턴
		if self.__len__() == 0: #빈 heap이면 None을 리턴한다
			return None
		else: #빈 heap이 아니라면 root 노드를 리턴한다
			return self.A[0]

	def delete_min(self): 
		# 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
		if self.__len__() == 0: #빈 heap이면 None 리턴
			return None
		self.D[self.A[len(self.A)-1]] = 0 #마지막 값의 인덱스를 0으로 저장
		self.D[self.A[0]] = len(self.A)-1 #그에따라 index값도 변경
		
		key = self.A[0] #key에 최소값(root node) 저장
		self.A[0] = self.A[self.__len__() - 1] #A리스트의 첫번째 값과 마지막 값을 바꿔줌
		self.A[self.__len__() - 1] = key
		
		self.A.pop() #A리스트 마지막에 있는 값을 삭제
		del(self.D[key]) # 그 값의 딕셔너리도 삭제
		
		self.heapify_down(0) #heapify_down으로 올라왔던 마지막 값때문에 흐트러진 힙을 다시 정렬
		
		return key #삭제했던 min값을 리턴

	def update_key(self, old_key, new_key):
		# 아니면, new_key 값이 최종 저장된 index 리턴
		if old_key not in self.D: #old_key가 heap에 없으면 None을 리턴한다
			return None
		else: #아니라면, new_key값이 최종저장된 index를 리턴한다
			self.A[self.D[old_key]] = new_key #원래 oldkey가 있던 인덱스에 newkey를 넣기
			self.D[new_key] = self.D[old_key] #그에따른 index도 변경해주기
			del(self.D[old_key]) #old_key의 index는 삭제
			self.heapify_up(self.D[new_key]) #heapify_up과 heapify_down을 통해 new_key의 위치 조정
			self.heapify_down(self.D[new_key])
			return self.D[new_key] #최종 저장된 index를 리턴한다
		
	
# 아래 명령 처리 부분은 수정하지 말 것!
H = AdaptedHeap()
while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		key = int(cmd[1])
		loc = H.insert(key)
		print(f"+ {int(cmd[1])} is inserted")
	elif cmd[0] == 'find_min':
		m_key = H.find_min()
		if m_key != None:
			print(f"* {m_key} is the minimum")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'delete_min':
		m_key = H.delete_min()
		if m_key != None:
			print(f"* {m_key} is the minimum, then deleted")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'update':
		old_key, new_key = int(cmd[1]), int(cmd[2])
		idx = H.update_key(old_key, new_key)
		if idx == None:
			print(f"* {old_key} is not in heap")
		else:
			print(f"~ {old_key} is updated to {new_key}")
	elif cmd[0] == 'print':
		print(H)
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")
