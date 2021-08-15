class Stack:#Stack 클래스 정의
	def __init__(self):#클래스의 생성자
		self.items = []
	def push(self, val):#self에 val을 추가한다
		self.items.append(val)
	def pop(self):#self에서 원소를 pop한다
		try:
			return self.items.pop()
		except IndexError:#IndexError라면 Stack이 비어있다는 오류 메세지를 출력
			print("Stack is empty")
	def top(self):#self의 제일 위에 있는 원소
		try:
			return self.items[-1]#마지막으로 들어온 것이므로 인덱스는 -1이다
		except IndexError:#IndexError라면 Stack이 비어있다는 오류 메세지를 출력
			print("Stack is empty")
	def __len__(self):#self의 길이를 반환
		return len(self.items)
	def isEmpty(self):#self가 비어있으면 True를 반환
		return self.__len__() == 0
	
def get_token_list(expr):
	result = expr.split(' ')
	return result
	
def compute_postfix(postfix):
	S = Stack()#결과를 담을 리스트
	for token in postfix:#token_list에 있는 토큰들을 차례대로 살펴봄
		if token == '+':#+연산자 이면 S에 있는 위에 두 숫자를 계산하여
			a = S.pop()
			b = S.pop()
			result = b + a#result에 담고
			S.push(result)#S에 다시 result를 추가한다.
		elif token == '-':#-연산자 이면 S에 있는 위에 두 숫자를 계산하여
			a = S.pop()
			b = S.pop()
			result = b - a#result에 담고
			S.push(result)#S에 다시 result를 추가한다.
		elif token == '*':#*연산자 이면 S에 있는 위에 두 숫자를 계산하여
			a = S.pop()
			b = S.pop()
			result = b * a#result에 담고
			S.push(result)#S에 다시 result를 추가한다.
		elif token == '/':#/연산자 이면 S에 있는 위에 두 숫자를 계산하여
			a = S.pop()
			b = S.pop()
			result = b / a#result에 담고
			S.push(result)#S에 다시 result를 추가한다.
		elif token == '^':#^연산자 이면 S에 있는 위에 두 숫자를 계산하여
			a = S.pop()
			b = S.pop()
			result = b ** a#result에 담고
			S.push(result)#S에 다시 result를 추가한다.
		else:#연산자가 아닌 숫자라면
			S.push(float(token))#token을 S에 추가
	return(S.pop())	#맨 마지막에 남아있는 S를 pop하여 리턴

expr = input()
value = compute_postfix(get_token_list(expr))
print('%.4f' %value)
