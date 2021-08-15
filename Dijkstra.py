import sys
class AdaptedHeap: # min_heap으로 정의함!
	def __init__(self):
		self.A = []
		self.D = {}  # dictionary D[key] = index

	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)
	
	def make_heap(self):
		n = len(self.A)
		for k in range(n-1, -1, -1):
			self.heapify_down(k,n) #리프노드


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




def Dijkstra(n, cost): #n은 정점수 cost는 정보가 들어있는 리스트
			s = 0 #source, 시작 노드(여기서는 0을 기본 시작 노드라고 가정)
			d = [inf] * n #d에는 source인 0부터의 최소한의 거리 저장
			d[0] = 0 #d = [0, inf, ... , inf]
			parent = [None] * n
			parent[0] = 0 #parent = [0, NULL, ..., NULL]
			H = AdaptedHeap() #dist로 힙을 만듦
			for i in range(n): #d 값들을 힙에 삽입해줌
				H.insert(d[i])
			while len(H): # n iterations len(H)
				u = H.delete_min() #dist의 최소값 리턴
				if u == inf: break
				for i in range(n):#이 최소 dist가 어느 노드의 dist 찾기
					if d[i] == u:
						j = i #노드의 번호를 j에 저장
						break
				#j와 인접한 i에 대해  j->i 
				result = 0
				for j in range(n):
					count = 0	
					for i in range(n):
						try:
							if cost[j][i] != 'inf': #cost[j][i]가 존재한다면(엣지가 존재한다면)
								if d[j] + cost[j][i] < d[i]: #relax
									d[i] = d[j] + cost[j][i] #값 업데이트
									H.insert(d[i])
									parent[i] = j
									H.heapify_up(d[i]) #decreaseKey(v, d[v])
									#heapify_up을 한번이라도 했다면 count를 1로 바꿔줌
									count += 1
						except Exception:
							continue
					#만약에 count = 0이 n번 출력되면 탐색을 그만둠
					if count == 0: result += 1
				if result == n: break #result 값이 n이 되면 while문을 아예 빠져나옴
			return d


if __name__ == "__main__":
	n = int(input())	#노드의 개수
	m = int(input())  #엣지의 개수
	inf = sys.maxsize
	cost = [['inf']*n for _ in range(n)]
	for i in range(m):
		u, v , w = map(int, input().split()) #3개 요소 입력
		cost[u][v] = w
	
	d = Dijkstra(n,cost) #리스트를 리턴받음
	for i in range(n):
		if d[i] == inf:
			print('inf', end= " ")
		else:
			print(d[i], end = " ")
