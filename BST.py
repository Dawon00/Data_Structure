# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
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

    
    def find_loc(self, key):
      if self.size == 0: return None
      p = None
      v = self.root
      while v:
        if v.key == key: return v
        else:
          if v.key < key:
            p = v
            v = v.right
          else:
            p = v
            v = v.left
      return p #찾는 키가 없으면 삽입될 곳의 부모노드 리턴


    def search(self, key):
      p = self.find_loc(key)
      if p and p.key == key:
        return p
      else:
        return None


    def insert(self, key):
      # key가 이미 트리에 있다면 에러 출력없이 None만 리턴!
      v = Node(key)
      if self.size == 0:
        self.root = v
      else:
        p = self.find_loc(key)
        if p and p.key != key :
          if p.key < key: p.right = v
          else: p.left = v
          v.parent = p
      self.size += 1
      return v


    def deleteByMerging(self, x):
        a = x.left
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
        return s


    def deleteByCopying(self, x):
      pt, L, R = x.parent, x.left, x.right
      if L: # L이 있음`
        y = x.left
        while y.right:
          y = y.right
        x.key = y.key
        if y.left:
          y.left.parent = y.parent
        if y.parent.left is y:
          y.parent.left = y.left
        else:
          y.parent.right= y.left
        del y

      elif not L and R: # R만 있음
        y = R
        while y.left:
          y = y.left
        x.key = y.key
        if y.right:
          y.right.parent = y.parent
        if y.parent.left is y:
          y.parent.left = y.right
        else:
          y.parent.right = y.right
        del y

      else: # L도 R도 없음
        if pt == None: # x가 루트노드인 경우
          self.root = None
        else:
          if pt.left is x:
            pt.left = None
          else:
            pt.right = None
        del x

T = Tree()

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
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
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
