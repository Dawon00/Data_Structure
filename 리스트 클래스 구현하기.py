	class myList():
	def __init__(self):
		self.capacity = 2	  # myList의 용량 (저장할 수 있는 원소 개수)
		self.n = 0          # 실제 저장된 값의 개수
		self.A = [None] * self.capacity # 실제 저장 자료구조 (python의 리스트 사용) 

	def __len__(self):
		return self.n
	
	def __str__(self):
		return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'

  
  def size(self):#용량을 알려주는 메소드
		return self.capacity #capacity를 리턴함
	
	def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
		return self.A[k]


	def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
		self.A[k] = x

	def change_size(self, new_capacity): #용량을 수정하는 메소드
		print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
		# 2. self.A의 값을 B로 옮김
		# 3. del self.A  (A 지움)
		# 4. self.A = B
		# 5. self.capacity = new_capacity
		B = [None] * (new_capacity) #new_capacity 크기의 리스트 B를 만든다
		for i in range(0, self.n): #A의 i번째에 있는 원소를 B의 i번째에 옮겨 넣는다
			B[i] = self.A[i]
		del self.A # 기존 A는 없애주고
		self.A = B #B를 A자리에 넣어준다
		self.capacity = new_capacity #capacity의 값을 업데이트 해준다
	
	def append(self, x): #맨 뒤에 원소를 추가해주는 메소드
		if self.n == self.capacity: # 만약에 원소의 개수랑 용량이 같다면 
			self.change_size(self.capacity * 2)# 더이상 넣을 공간이 없으므로 capacity를 2배로 doubling 해준다
		self.A[self.n] = x     # 맨 뒤에 삽입
		self.n += 1            # n 값 1 증가


	def pop(self, k=None): # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴
		if k < 0: #음수 인덱스가 들어오면
				k = self.n + k #양수 인덱스로 바꾸어 고려한다
		if ((self.n == 0) or (k >= self.capacity)): # 빈 리스트이거나 올바른 인덱스 범위를 벗어나면:
			raise IndexError #IndexError
		if self.capacity >= 4 and self.n <= self.capacity//4: # 실제 key 값이 전체의 25% 이하면 halving
			self.change_size(self.capacity//2)
		# 1. k 값이 주어진 경우와 주어지지 않은 경우 구별해야 함
		# 2. x = self.A[k]
		# 3. A[k]의 오른쪽의 값들이 한 칸씩 왼쪽으로 이동해 메꿈
		# 4. self.n -= 1
		# 5. return x
		if (k == -1): #k값이 주어지지 않았다면
			if self.A[self.n-1] == None:#만약에 마지막 원소가 None인 경우가 있다면
				raise IndexError#IndexError
			x = self.A[self.n-1] #마지막 원소를 x에 넣어준다
			self.A[self.n-1] = None #마지막 원소를 None 으로 바꿔준다
			self.n -= 1 #원소 개수를 하나 줄인다
			return x #아까 저장해놨던 마지막 원소를 리턴한다
		else: #k값이 주어졌다면
			if self.A[k] == None: #만약 k인덱스 원소가 None이라면
				raise IndexError #IndexError
			x = self.A[k]#k인덱스 원소를 x에 넣는다
			self.A[k] = None#k인덱스 원소를 None으로 만들어 준다
			for i in range(k, self.n-1):#지운 원소 오른쪽에 있는 원소들을 한칸씩 왼쪽으로 이동시킨다
				self.A[i] = self.A[i+1]
			self.n -= 1#원소의 개수를 하나 줄인다
			return x#k인덱스 원소를 리턴한다

	def insert(self, k, x):#k인덱스에 x를 삽입하는 메소드
		if k < 0:#만약에 음수 인덱스이면
				k = self.n + k#양수 인덱스로 바꿔서 생각합니다
		# 주의: k 값이 음수값일 수도 있음
		# k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
		# 1. k의 범위가 올바르지 않으면 IndexError 발생시킴
		# 2. self.n == self.capacity이면 self.change_size(self.capacity*2) 호출해 doubling
		# 3. A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
		# 4. self.A[k] = x
		# 5. self.n += 1
		if (self.n == 0 or k >= self.capacity): # **빈리스트 이거나**올바른 인덱스 범위를 벗어나면:
			raise IndexError #IndexError
		if self.n == self.capacity: #만약에 원소의 개수와 용량이 같다면
			self.change_size(self.capacity * 2)#용량을 두배로 늘린다
		for i in range(self.n-1, k-1,-1):#삼입을 했으면 그 삽입한 원소 오른쪽에 있는 원소들은 오른쪽으로 한칸씩 이동시킨다
			self.A[i+1] = self.A[i]
		self.A[k] = x#x값을 k인덱스에 저장함
		self.n += 1#원소의 개수를 하나 늘린다
    
    L = myList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'pop':
        if len(cmd) == 1:
            idx = -1
        else:
            idx = int(cmd[1])
        try:
            x = L.pop(idx)
            print(f"  - {x} at {idx} is popped.")
        except IndexError:
            if len(L) == 0:
                print("  ! list is empty.")
            else:
                print(f"  ! {idx} is an invalid index.")
    elif cmd[0] == 'insert':
        try:
            L.insert(int(cmd[1]), int(cmd[2]))
            print(f"  + {cmd[2]} is inserted at index {cmd[1]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'get': # getitem A[k]
        try:
            L[int(cmd[1])]
            print(f"  @ L[{cmd[1]}] --> {L[int(cmd[1])]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'set': # setitem A[k] = x
        try:
            L[(int(cmd[1]))] = int(cmd[2])
            print(f"  ^ L[{cmd[1]}] <-- {cmd[2]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'size':
        print("  ? capacity =", L.size())
    elif cmd[0] == 'print':
        print(L)
    elif cmd[0] == 'exit':
        print('bye~')
        break
    else:
        print(" ? invalid command! Try again.")
