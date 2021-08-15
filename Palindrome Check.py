class deque:
	def __init__(self, string):
		self.items = []
		for i in range(len(string)):
			self.items.append(string[i])
	
	def append(self, c):
		self.items.append(c)
	
	def appendleft(self, c):
		self.items.insert(0, c)
	
	def pop(self):
		return self.items.pop()
	
	def popleft(self):
		temp = self.items[0]
		del self.items[0]
		return temp
	
	def __len__(self):
		return len(self.items)
	
	def right(self):
		return self.items[-1]
	
	def left(self):
		return self.items[0]

def check_palindrome(s):
	dq = deque(s)#생성과 동시, 문자열 보냄
	palindrome = True#초기값은 True
	while len(dq) > 1:#짝수 0개남음 / 홀수 1개 남음
		if dq.popleft() != dq.pop():#양쪽으로 꺼내서 비교
			palindrome = False#다르면 False
			return palindrome
	return palindrome#모두 같아서 True 반환

s = input()
print(check_palindrome(s))
​
