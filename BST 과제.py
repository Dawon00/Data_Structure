class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v): #MLR
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v): #LMR
      if v != None:
        self.inorder(v.left)
        print(v.key, end=' ')
        self.inorder(v.right)


    def postorder(self, v): #LRM
      if v != None:
        self.postorder(v.left)
        self.postorder(v.right)
        print(v.key, end=' ')


    def find_loc(self, key): #key값의 자리를 찾아주는 함수
      if self.size == 0: return None #비어있으면 return None
      p = None
      v = self.root
      while v:
        if v.key == key: return v #만약 key와 같은 값을 찾으면 return v
        else:
          if v.key < key: #key보다 작으면 오른쪽으로 이동
            p = v
            v = v.right
          else: #그렇지 않으면 왼쪽으로 이동
            p = v
            v = v.left
      return p #찾는 키가 없으면 삽입될 곳의 부모노드 리턴


    def search(self, key): #key가 있는지 확인하고 있다면 find_loc의 결과를 리턴, 없다면 None 리턴
      p = self.find_loc(key)
      if p and p.key == key:
        return p
      else:
        return None

    def update_height(self, x): #height을 업데이트 해주는 함수
        if x == None: #x가 존재하지 않으면 None 리턴
           return None
        while x != None: #x가 존재할때
            if x.left: #왼쪽 자식노드가 있으면
               Lh = x.left.height #왼쪽 자식노드의 높이를 LH에 넣기
            else:
               Lh = -1 #왼쪽자식노드가 존재하지 않는경우(None 인경우)-1
            if x.right != None: #오른쪽 자식 노드가 있으면
               Rh = x.right.height #오른쪽 자식 노드의 높이를 RH에 넣기
            else:
               Rh = -1 #오른쪽자식노드가 존재하지 않는경우(None 인경우)-1
            if Lh < Rh: #x 노드의 height은 오른쪽, 왼쪽 중 더 긴 쪽의 +1을 한 값
                 x.height = Rh + 1
            else:
                 x.height = Lh + 1
            x = x.parent #부모노드로 이동하며 반복함

    def insert(self, key):
      v = Node(key) #key값을 가지는 노드 v를 만든다
      if self.size == 0: #비어있는 트리라면 루트노드가 된다
        self.root = v
        v.height = 0
      else:
        p = self.find_loc(key) #key가 자식노드로써 들어갈 부모노드 p를 찾음
        if p and p.key != key : #p가 존재하고, p의 기존key와 key가 다르면
          if p.key < key: #key가 더 크면 p의 오른쪽에 넣고 key 가 더 작으면 p의 왼쪽에 넣기
            p.right = v
          else: #아니라면 왼쪽에 넣기
            p.left = v
          v.parent = p #p를 v의 부모노드로 연결
        self.update_height(p)
      self.size += 1 #사이즈를 하나 증가시키기
        # 노드들의 height 정보 update 필요
      return v

    def deleteByMerging(self, x):
        a = x.left #a는 x의 왼쪽 자식노드, y는 오른쪽 자식노드. pt는 부모노드
        b = x.right
        pt = x.parent
        #c = x위치에 있는 노드
        #s = 균형이 깨진 첫번째 노드
        if a == None: #왼쪽 노드가 비어있으면 오른쪽으로 내려가기
          c = b
          s = pt
        else: #왼쪽노드에 뭔가 있으면 왼쪽으로 내려가기
          c = m = a
          while m.right: #a 부트리 맨 오른쪽 자식노드 m
            m = m.right
          m.right = b #그 m에 b을 오른쪽 자식노드로 달아줌
          if b: #b의 부모노드를 m으로 연결
            b.parent = m
          s = m #균형이 깨진 첫노드를 m으로
        if self.root == x: #만약에 x가 root노드면 c의 부모에 None 넣어주고 root에는 c넣어줌
          if c:
            c.parent = None
          self.root = c
        else: #x가 root가 아닌경우
          if pt.left == x: #x가 왼쪽 자식노드라면
            pt.left = c
          else:  #x가 오른쪽 자식노드라면
            pt.right = c
          if c: 
            c.parent = pt
        self.size -= 1
        # 노드들의 height 정보 update 필요
        self.update_height(b)
        return s #균형이 깨진 첫번째 노드 리턴

      def deleteByCopying(self, x):
      pt, L, R = x.parent, x.left, x.right
      if L: # L이 있음`
        y = x.left #y는 L에서 가장 큰값
        while y.right: #y의 오른쪽자식노드 존재한다면 오른쪽으로 이동
          y = y.right
        x.key = y.key #x의 key에 y의 key를 넣어줌
        if y.left: #y의 왼쪽자식 존재하면 y의 왼쪽 부모에 y의 부모넣어줌
          y.left.parent = y.parent
        if y.parent.left is y: #y 부모의 왼쪽이 y라면 y의 왼쪽을 y 부모 왼쪽에 넣어줌
          y.parent.left = y.left
        else: #위에 해당이 안된다면 y의 왼쪽을 y의 부모 오른쪽에 넣어줌
          y.parent.right= y.left
         #height 값 수정
        self.update_height(y)
        del y

      elif not L and R: # R만 있음
        y = R
        while y.left: #y의 왼쪽이 있는 한 반복
          y = y.left #y왼쪽으로 이동
        x.key = y.key#y의 key를 x에 넣어줌
        if y.right: #y의 오른쪽 존재한다면 y의 부모를 y의 오른쪽자식의 부모에 넣음
          y.right.parent = y.parent
        if y.parent.left is y: #y의 부모의 왼쪽자식이 y면 y의 오른쪽자식을 y의 부모의 왼쪽 자식에 넣음
          y.parent.left = y.right
        else: #위에 해당이 안되면 y의 오른쪽 자식을 y의 부모의 오른쪽 자식에 넣음
          y.parent.right = y.right
           #height값 수정하기
        self.update_height(y)
        del y

      else: # L도 R도 없음
        if pt == None: # x가 루트노드인 경우
          self.root = None
        else: #x가 루트노드가 아닌경우
          if pt.left is x: #pt의 왼쪽이 x인경우 pt의 왼쪽을 None으로 만들어줌
            pt.left = None
          else: #pt의 오른쪽이 x인 경우 pt의 오른쪽을 None으로 만들어줌
            pt.right = None
        # 노드들의 height 정보 update 필요
        self.update_height(pt)
        del x
      self.size -= 1 #사이즈를 하나 줄이기


    def height(self, x): # 노드 x의 height 값을 리턴
        if x == None: #x가 None이면 -1 리턴하고 아니면 height 리턴
          return -1
        else: 
          return x.height



    def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        if x.right: #R이 존재한다면
          suc = x.right #x의 R부터 시작해서 맨 왼쪽 아래까지 내려감
          while suc.left != None: #None 아닐때까지(리프노드까지 내려감)
            suc = suc.left
          return suc #맨마지막 리프노드가 우리가 찾는 succ
        elif x.right == None and x.parent: #내려갈 R이 없다면 부모노드로 타고 올라가면서 찾기
          suc = x.parent
          while suc != None: #root 노드를 넘어서기 전까지 반복
            if suc.key < x.key: #x보다 작으면 패스
              suc = suc.parent
              continue
            else: #x보다 큰 값을 찾으면 그게 바로 succ
              return suc
          return None #끝까지 올라갔는데도 없었으면 return None
        else: #내려갈 곳도 올라갈 곳도 없다면 None
          return None



    def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        if x.left: #L이 존재한다면
          pre = x.left #x의 L부터 시작해서 맨 오른쪽 아래까지 내려감
          while pre.right != None:#None 아닐때까지(리프노드까지 내려감)
            pre = pre.right
          return pre #맨마지막 리프노드가 우리가 찾는 succ
        elif x.left == None and x.parent: #내려갈 L이 없다면 부모노드로 타고 올라가면서 찾기
          pre = x.parent
          while pre != None:
            if pre.key > x.key: #x보다 크면 패스
              pre = pre.parent
              continue
            else: #x보다 작은 값을 찾으면 그게 바로 pred
              return pre
          return None
        else: #내려갈 곳도 올라갈 곳도 없다면 None
          return None



    def rotateLeft(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
      if not x: return 
      z = x.right #z는 x의 오른쪽 자식노드
      if z == None: return #z가 없다면 None리턴
      b = z.left #b는 z의 왼쪽 자식노드
      z.parent = x.parent #x의 부모를 z 부모에 너어줌
      if x.parent: #x의 부모가 있다면
        if x.parent.left == x: #x 부모의 왼쪽이 x라면 x를 x의 부모 왼쪽에 넣어줌
          x.parent.left = x
        else: #아니라면 x의 부모 오른쪽에 x 넣기
          x.parent.right = x
      z.left = x #z의 왼쪽에 x넣고 x의 부모에 z넣고, x의 오른쪽에 b넣기
      x.parent = z
      x.right = b
      if b: #b가 있다면 b의 부모는 x
        b.parent = x
      #x == self.root라면 z가 새로운 루트가 되어야함
      if x == self.root: #x가 루트노드라면 z를 root에 넣어줌
        self.root = z
      #x와 z height 수정
      self.update_height(x)



    def rotateRight(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
      if not z: 
          return #if z == None check
      x = z.left #z의 왼쪽 자식을 x라고 하자
      if x == None: 
          return
      b = x.right
      x.parent = z.parent #z의 parent 였던게 x의 parent가 됨
      if z.parent: #z의 부모가 있다면
        if z.parent.left == z: #z의 부모 왼쪽이 z라면 z의 부모 왼쪽에 x넣기
          z.parent.left = x
        else:#아니라면 z의 부모 오른쪽에 x넣기
          z.parent.right = x
      x.right = z #x오른쪽에 z넣고, z 부모에 x넣고, z왼쪽에 b 넣기
      z.parent = x
      z.left = b
      if b: #b가 있다면 b의 부모에 z 넣기
        b.parent = z
      #z == self.root라면 x가 새로운 루트가 되어야함
      if z == self.root and x != None:
        self.root = x
      #x와 z의 height 값 수정하는 코드 추가
      self.update_height(z)
      
      
T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")

      
