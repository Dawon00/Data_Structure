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

    def update_height(self, v): #height을 업데이트 해주는 함수
      while v != None: #v가 존재할때 v의 왼쪽 자식노드의 높이를 l, 오른쪽 자식노드의 높이를 r로 설정
        l, r = -1, -1
        if v.left:
          l = v.left.height
        if v.right:
          r = v.right.height
        v.height = max(l, r) + 1 #l과 r중 큰 값에 1을 더한 것이 v의 높이
        v = v.parent #v의 부모노드로 이동

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
        self.update_height(p) #노드 p의 높이를 업데이트
      self.size += 1 #사이즈를 하나 증가시키기
      return v

    def deleteByMerging(self, x):
        if x == None:
          return None
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
        del x
        self.size -= 1
        # 노드들의 height 정보 update 필요
        self.update_height(s)
        return s #균형이 깨진 첫번째 노드 리턴


    def deleteByCopying(self, x):
      if x == None: #x가 None이면 None을 리턴한다
        return None
      a = x.left #a는 x의 왼쪽자식
      if a == None: #왼쪽이 없으면 b가 x의 오른쪽, pt는 x의 부모
        b, pt = x.right, x.parent
        if pt == None: #부모가 없으면 b가 루트노드
          self.root = b
        else: #부모가 있다면
          if pt.left == x: #부모의 왼쪽에 있는게 x라면 pt의 왼쪽을 b
            pt.left = b
          else: #오른쪽에 있는게 x라면 pt의 오른쪽을 b
            pt.right = b
        if b: #b가 존재하면 b의 부모는 pt
          b.parent = pt
        del x #x 삭제
      else: #a != None
        m = a #m은 a부터 시작해서 최대한 오른쪽 자식으로 이동
        while m.right:
          m = m.right
        x.key = m.key #m의 key를 x의 key에 대입하고 l은 m의 왼쪽, pt는 m의 부모로 설정
        l, pt = m.left, m.parent
        if pt.left == m: #pt의 왼쪽이 m이면 l을 pt의 왼쪽이라고 해주고 아니면 l을 pt의 오른쪽으로 설정
          pt.left = l
        else:
          pt.right = l
        if l: #l이 존재하면 pt를 l의 부모로 설정하고 m을 삭제
          l.parent = pt
        del m
      self.size -= 1 #사이즈를 하나 줄여주고 pt의 높이도 업데이트
      self.update_height(pt)
      return pt


    def height(self, x): # 노드 x의 height 값을 리턴
        if x == None: #x가 None이면 -1 리턴하고 아니면 height 리턴
          return -1
        else: 
          return x.height



    def succ(self, x): # 바로 다음 크기 값
      if x == None or self.size == 1:
        return None
      r = x.right #서브 R 이 있으면 R의 최소를 찾음
      while r and r.left:
        r = r.left
      if r:
        return r
      else: #r이 없으면 본인이 올라가다 왼쪽 자식일때에 멈춤
        pr = x.parent
        while pr and pr.right == x:
          x = pr
          pr = pr.parent
        return pr #그 때의 부모
  def pred(self, x): # 바로 전 크기값
      if x == None or self.size == 1:
        return None
      r = x.left #서브 L이 있으면 L의 최대를 찾는다
      while r and r.right:
        r = r.right
      if r:
        return r
      else: #서브 L이 없으면 본인이 오른쪽 자식일때 stop
        pr = x.parent
        while pr and pr.left == x:
          x = pr
          pr = x.parent
        return pr #그 부모 리턴



    def rotateLeft(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요) 
      z = x.right #z는 x의 오른쪽 자식노드
      if z == None: 
        return #z가 없다면 None리턴
      b = z.left #b는 z의 왼쪽 자식노드
      z.parent = x.parent #x의 부모를 z 부모에 너어줌
      if x.parent: #x의 부모가 있다면
        if x.parent.left == x: #x 부모의 왼쪽이 x라면 x를 x의 부모 왼쪽에 넣어줌
          x.parent.left = z
        else: #아니라면 x의 부모 오른쪽에 x 넣기
          x.parent.right = z
      if z: #z가 존재하면 x을 z의 왼쪽이라고 설정
        z.left = x
      x.parent = z #z는 x의부모, b는 x의 오른쪽
      x.right = b
      if b: #b가 존재한다면 b의 부모는 x
        b.parent = x
      if self.root == x and z != None: #x가 루트노드이거나 z가 None이 아니라면 z를 루트노드라고 한다
        self.root = z
      self.update_height(x) #높이를 업데이트 해줌



    def rotateRight(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
      x = z.left #x는 z의 왼쪽노드
      if x == None: #x가 존재하지 않으면 None리턴
        return
      b = x.right #b는 x의 오른쪽, z의 부모를 x의 부모라고 설정
      x.parent = z.parent
      if z.parent: #z의 부모가 존재하는데 z가 z의 부모 왼쪽과 같다면 x를 z의 부모 왼쪽이라고 설정, 아니면 z 부모의 오른쪽으로 설정
        if z.parent.left == z:
          z.parent.left = x
        if z.parent.right == z:
          z.parent.right = x
      if x: #x가 존재하면 x의 오른쪽을 z라고 설정하고 z의 부모를 x, z의 왼쪽을 b라고 해준다
        x.right = z
      z.parent = x
      z.left = b
      if b: #만약 b가 존재하면 b의 부모는 z, 만약 z가 루트노드이거나 x가 None이 아니라면 x를 루트노드라고 설정
        b.parent = z
      if self.root == z and x != None:
        self.root = x
      self.update_height(z) #z의 높이 업데이트


class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def rebalance(self, x, y, z):
        if x == None or y == None or z == None: #x,y,z는 None이 아님
          return None
        # rotate 후에는 top 노드를 리턴한다
        # z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음
        if self.balance_factor(z) <= -2 or self.balance_factor(z) >= 2: #rebalance가 필요하다면(4가지 경우에 따라 rotate)
          #case 1
          if y == z.left:
            if x == z.left.left:
              self.rotateRight(z)
              return y
            #case 3
            elif x == z.left.right:
              self.rotateLeft(y)
              self.rotateRight(z)
              return x
          #case 2
          elif y == z.right:
            if x == z.right.right:
              self.rotateLeft(y)
              return y
            #case 4
            elif x == z.right.left:
              self.rotateRight(y)
              self.rotateLeft(z)
              return x


    def balance_factor(self, x): #양쪽 자식노드의 높이 차이를 리턴해주는 함수
      if x == None:
        return 0
      return self.height(x.left) - self.height(x.right)

    def insert(self, key):
        # BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 
        # super(class_name, instance_name).method()으로 호출
        # 새로운 삽입된 노드가 리턴됨
        v = super(AVL, self).insert(key)
        temp = v
        # x, y, z를 찾아 rebalance(x, y, z)를 호출
        #새로 삽입된 노드에서부터 타고 올라가면서 AVL 조건이 깨진 노드를 찾는다.
        while v != None: #v는 부모노드를 타고 올라가며 root 노드까지 확인한다
          #print(v,'의 balance_factor 값은', self.balance_factor(v))
          if self.balance_factor(v) >= 2 or self.balance_factor(v) <= -2: #조건이 깨진 노드를 찾는다면 그 노드를 z라고 하자
            #print('깨진 노드를 찾았다')
            z = v
            #y와 x 정하기
            if self.balance_factor(z) > 0: #양수면 왼쪽이 더 무겁다는 얘기
              y = z.left
            else:
              y = z.right
            if self.balance_factor(y) > 0: #양수면 왼쪽이 더 무겁다는 얘기
              x = y.left
            else:
              x = y.right
            w = self.rebalance(x,y,z) #top 노드가 리턴됨
            #print('top노드는 ', w)
            if w.parent == None: #w가 만약 루트 노드이면 루트노드 갱신
              self.root = w
          else: #아니라면 다음 부모노드로 올라간다
            v = v.parent
        return temp
        
            def delete(self, u): # delete the node u
        v = super(AVL,self).deleteByCopying(u) # 또는 self.deleteByMerging을 호출. 이 과제에서는 채점을 위해 deleteByCopying을 호출한다
        # height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장
        while v != None:
            # v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
            # z - y - x를 정한 후, rebalance(x, y, z)을 호출
            self.update_height(v)
            if self.balance_factor(v) >= 2 or self.balance_factor(v) <= -2:
              z = v
              if self.balance_factor(z) >=  0: #양수면 왼쪽이 더 무겁다는 얘기
                y = z.left
              else:
                y = z.right
              if self.balance_factor(y) >=  0: #양수면 왼쪽이 더 무겁다는 얘기
                x = y.left
              else:
                x = y.right
              v = self.rebalance(x,y,z)
            w = v
            v = v.parent #v는 부모노드로 올라가고 루트노드를 w로 설정
            self.root = w



T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
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
 
