class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key): #key가 존재할경우 해당 슬롯 번호를 리턴
        i = int(self.hash_function(key)) #i가 float여서 int형으로 바꿔줌. i를 key의 해시함수 값이라 하고 이 값을 start에 저장
        start = i 
        while(self.keys[i] != None and self.keys[i] != key): #슬롯이 차있거나 key를 찾으면 빠져나오는 반복문
            i = int((i+1) % self.size) #i는 다음칸으로 이동
            if i == start : #한바퀴를 돌았다. 테이블이 full이다. key 값을 갖는 슬롯도 없다
                return None #None리턴
        return i #key가 존재한다면 그 슬롯 번호, key가 없다면 새로 삽입할 슬롯 번호

    def set(self, key, value=None): #새로운 값을 저장해주는 함수, key리턴
        i = self.find_slot(key) #key의 슬롯번호를 i라고 한다
        if i == None:#빈슬롯이 없다면 None을 리턴한다
            return None
        if self.keys[i] != None: #key값이 존재하면 value를 수정한다
            self.values[i] = value #value를 업데이트 한다
        else: #H[i]가 비어있는 경우(=key가 없는 경우) 새로 저장한다
            self.keys[i], self.values[i] = key, value
        return key

    def hash_function(self, key): #해시함수 만들어 주기. key값을 size로 나눈 나머지를 리턴
        return key % self.size

    def remove(self, key): #key를 삭제해주는 함수. key가 존재할경우 삭제하고 아니면 None리턴
      #i는 빈슬롯이 되고 j에 있는 아이템을 i로 옮길지 말지를 결정하게 된다. 옮긴다면 j가 빈슬롯이 된다
      i = int(self.find_slot(key))#i를 key의 슬롯번호라고 함
      if self.keys[i] == None:#key가 비어있으면 None을 리턴
        return None
      j=i
      while True:
        self.keys[i] = None
        while True:
          j=int((j+1) % self.size)
          if self.keys[j] == None:#비어있으면
            return key #제거하기 끝. key를 리턴한다
          k = self.hash_function(self.keys[j]) #j의 해시함수 값 k
          if not(i<k<=j or j<i<k or k<=j<i): #i,j,k의 순서가 조건을 만족하면 옮긴다
            break
        self.keys[i] = self.keys[j]#j에 있는 걸 i로 옮겨준다
        i = j

    def search(self, key):#key 존재하면 key(or value) 리턴, 없는 key면 None리턴
      i = self.find_slot(key) #find_slot으로 슬롯번호를 찾아준다
      if self.keys[i] != None: #key가 존재한다(i번째 슬롯이 차있다)
        return self.keys[i], self.values[i] #그 슬롯의 key와 value를 리턴한다
      else: #key가 존재하지 않으면 None을 리턴한다
        return None, None

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)



A = [int(x) for x in input().split()] #명수이 물건 리스트
B = [int(x) for x in input().split()] #재석이 물건 리스트
#
AH = HashOpenAddr() #AH라는 해시테이블을 만들어 명수 물건을 차례대로 AH에 넣는다
AH.__init__(int(len(A)*1.5)) #size(슬롯의 개수)는 입력되는 key의 1.5배로 설정
for x in A:#A에 있는 값을 AH에 하나씩 넣는다
  idx, value = AH.search(x) #x가 AH에 존재하는지 확인
  if idx == None:#만약 AH에 없는 key라면 새로 저장(value는 key의 빈도수이므로 처음엔 1로 설정)
    AH.set(x,1)
  else:#만약 AH에 이미 있는 key라면 value를 업데이트(1개 늘려줌)
    AH.values[idx] = value + 1



result = [] #첫번째 줄에 해당하는 리스트 result(재석이가 가진 물건중 명수가 가지고 있는 물건)
for x in B:#B에 있는 물건을 순서대로 확인
  idx, value = AH.search(x) #AH에 존재하는지 확인
  if idx == None: # 겹치는게 없으면 다음 번호로 넘어가기
    continue
  else: #겹치는게 있다. AH에서 삭제해주기
    if value > 1:#value가 1보다 큰경우 기존 value에서 1을 빼주고 x를 result에 추가해준다
      AH.values[idx] = value -1
      result.append(x)
    else : #value가 1개이면
      AH.remove(x) #AH에서 아예 삭제해주고
      result.append(x) #result에 x를 추가해줌

for i in range(0,len(result)): #첫번째 줄을 출력한다
  print(result[i], end=' ')

BH = HashOpenAddr()#BH 해시테이블을 만들어준다. 중복되는 물건을 지워주기 위한 과정
BH.__init__(int(len(result)*1.5))#size는 입력되는 개수의 1.5배로 설정
result2 = []#두번째 줄에 해당하는 리스트(재석이가 가진 물건중 명수가 가지고 있는 물건에서 중복물건을 제거해준 것)

for x in result:#result에 있는 물건들을 순서대로 확인
  idx, value = BH.search(x)#BH에 존재하는지 확인
  if idx == None: #새로운 key이면
    BH.set(x,1)#BH에 저장해준다. value는 key 빈도수이므로 처음엔 1로 설정한다
    result2.append(x)#result2 리스트에 x를 추가해준다
  else: # 존재하는 key라면 넘어간다
    continue
print()#줄바꿈

for i in range(0, len(result2)):#두번째 줄을 출력한다
  print(result2[i], end=' ')
