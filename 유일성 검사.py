import random, time

def unique_n2(A):#O(n^2) 시간에 동작하는 알고리즘
	for i in range(0, len(A)): #모든 원소를 하나씩 짝지어 비교한다.
		for j in range(i+1,len(A)):#모든 경우의 수를 만들어 비교하기 위해 이중 for 문을 사용한다.
			if A[i] == A[j]:#i번째 원소와 j번째 원소를 비교한다.
				return 'NO'#만약 조건을 만족하면 NO를 리턴한다
	return 'YES'#YES를 리턴한다
	
def unique_nlogn(A):#O(nlogn) 시간에 동작하는 알고리즘
	A.sort()#A리스트에 들어있는 수를 오름차순으로 정렬한다. O(nlogn)시간이 걸린다
	for i in range(0,len(A)-1):#i를 0부터 n-2까지 변화시킨다
		if A[i] == A[i+1]:#오름차순으로 정렬된 원소들을 두개씩 짝지어 같은지 비교한다.
			return 'NO'#만약 조건을 만족하면 NO를 리턴한다
	return 'YES'#YES를 리턴한다

def unique_n(A):#O(n)시간에 동작하는 알고리즘
	B=[]#빈 리스트를 생성
	temp = set()#중복을 허용하지 않는 set형으로 temp를 만든다
	for i in range(0,len(A)):#A에 있는 원소들을 순환하기 위해 인덱스 0부터 len(A)-1까지 i를 변화시킨다
		if A[i] not in temp:#temp에 A[i]가 존재하는지 확인한다
			temp.add(A[i])#없다면 temp에 A[i]를 추가한다
			B.append(A[i])#B리스트에도 A[i]를 추가한다
	if len(A) == len(B):#만약 A리스트와 B리스트의 길이가 같다면 중복이 없었다는 의미이므로
		return 'YES'#YES를 리턴한다
	else:#길이가 다르다면
		return 'NO'#NO를 리턴한다

n = int(input())#정수형으로 값의 개수인 n을 입력받는다
A = random.sample(range(-n, n+1), n)# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성

print(unique_n(A))# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
print(unique_n2(A))# 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다
print(unique_nlogn(A))

s= time.process_time()#unique_n(A)의 수행시간 측정, 현재 프로세서 시간 리턴
unique_n(A)#함수 호출
e = time.process_time()#s로부터 경과한 현재의 시간
print("수행시간 =",e-s)#수행시간 출력

s= time.process_time()#unique_nlogn(A)의 수행시간 측정
unique_nlogn(A)
e = time.process_time()
print("수행시간 =",e-s)

s= time.process_time()#unique_n2(A)의 수행시간 측정
unique_n2(A)
e = time.process_time()
print("수행시간 =",e-s)# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다
