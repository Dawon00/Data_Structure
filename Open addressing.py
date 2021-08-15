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
        i = self.hash_function(key)
        start = i
        while( self.keys[i] != None and self.keys[i] != key): #슬롯이 차있거나 key를 찾으면 빠져나오는 반복문
            i = (i+1) % self.size #i는 다음칸으로 이동
            if i == start : #한바퀴를 돌았다. 테이블이 full이다. key 값을 갖는 슬롯도 없다
                return None #None리턴
        return i #key가 존재한다면 그 슬롯 번호, key가 없다면 새로 삽입할 슬롯 번호

    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == None:#빈슬롯이 없다
            return None
        if self.keys[i] != None: #key값이 존재하면 기존값을 수정한다
            self.values[i] = value #value를 업데이트 한다
        else: #H[i]가 비어있는 경우(=key가 없는 경우) 새로 저장한다
            self.keys[i], self.values[i] = key, value
        return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
      i = self.find_slot(key)
      if self.keys[i] == None:#비어있으면
        return None
      j=i
      while True:
        self.keys[i] = None
        while True:
          j=(j+1) % self.size
          if self.keys[j] == None:#비어있으면
            return key
          k = self.hash_function(self.keys[j])
          if not(i<k<=j or j<i<k or k<=j<i):
            break
        self.keys[i] = self.keys[j]
        i = j

    def search(self, key):#key 존재하면 key(or value) 리턴, 아니면 None리턴
      i = self.find_slot(key)
      if self.keys[i] != None: #key가 존재한다(i번째 슬롯이 차있다)
        return self.keys[i] #그 슬롯의 key를 리턴한다
      else: #key가 존재하지 않는다
        return None

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)
        
H = HashOpenAddr()
while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        if key == None: print("* H is full!")
        else: print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
