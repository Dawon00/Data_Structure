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
	
def get_token_list(expr):#입력받은 수식을 token화 하기
	token_list = []#token_list라는 빈리스트를 생성
	temp = ""#실수을 만들기 위한 temp를 생성
	for i in range(len(expr)):#expr의 원소를 순환
		if (expr[i] == ".") or (expr[i].isdigit() == 1): #원소가 . 이거나 숫자라면
			temp += expr[i]#temp에 원소를 넣어둔다.
		elif expr[i] == " ": #빈칸이라면 패스
			pass
		else: #연산자라면
			if temp != "": #temp에 뭔가 있다면
				token_list.append(temp)#temp에 있는 걸 token_list에 추가
			token_list.append(expr[i])#i인덱스 원소를 token_list에 추가
			temp = ""#temp를 비우기
	token_list.append(temp)#마지막으로 temp에 담겨있던걸 token_list에 추가
	return (token_list)#token_list를 리턴합니다
	
def infix_to_postfix(token_list):#infix 형식을 postfix 형식으로 바꾸는 함수
	opstack = Stack()#연산자 넣을 스택
	outstack = []#빈리스트
	prec = {}#연산자들의 우선순위를 지정함
	prec['('] = 0
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 3
	
	for token in token_list:#token_list의 원소들을 차례대로 살펴봄
		if token == '' or token == ' ':#빈칸이거나 의미가 없는 토큰은 패스함
			continue
		elif token == '(':#왼쪽 괄호는 일단 opstack에 무조건 추가
			opstack.push(token)
		elif token == ')':#오른쪽 괄호를 마주치면 opstack에 있던 토큰을 모두 pop하고 outstack에 append
			while opstack.top() != '(':
				outstack.append(opstack.pop())
			opstack.pop()#opstack에 남아있는걸 pop
		elif token in '+-*/^':#연산자들 중 하나라면
			if opstack.isEmpty()==True:#opstack이 비어있다면
				opstack.push(token)#토큰을 append
			elif prec[token]>prec[opstack.top()]:#우선순위가 더 높다면
				opstack.push(token)#opstack에 토큰을 push
			else:
				while prec[opstack.top()]>=prec[token]:#token의 우선수위보다 opstack.top()의 우선순위가 크거나 같을때
					outstack.append(opstack.pop())#opstack에서 pop하여 outstack에 append
					if opstack.isEmpty() == True:#opstack이 비어있다면
						break#반복문을 빠져나온다
				opstack.push(token)#token을 opstack에 push한다
		else:#숫자라면
			outstack.append(token)#token을 outstack에 바로 추가
	while opstack.isEmpty() ==False:#opstack에 뭔가 남아있다면
		outstack.append(opstack.pop())#opstack에서 pop하여 outstack에 추가해준다
	return(outstack)#완성된 outstack을 리턴

def compute_postfix(token_list):#postfix를 계산하는 함수
	S = Stack()#결과를 담을 리스트
	for token in token_list:#token_list에 있는 토큰들을 차례대로 살펴봄
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
	
	
# 아래 세 줄은 수정하지 말 것!
expr = input() #수식을 입력받는다
value = compute_postfix(infix_to_postfix(get_token_list(expr)))#함수를 이용하여 수식을 계산, value변수에 결과값을 담는다
print(value)#value를 출력한다
