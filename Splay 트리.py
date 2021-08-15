class Node:
    def __init__(self, key = None, parent = None, left=None, right=None):
      self.key = key
      self.parent = parent
      self.left = left
      self.right = right
      self.height = 0

    def __str__(self):
      return str(self.key)

    def __iter__(self):
      if self:
        if self.left:
          for elm in self.left:
            yield elm
        yield self.key
        if self.right:
          for elm in self.right:
            yield elm

    def _right_height(self):
      if self.right: return self.right.height
      return -1
    def _left_height(self):
      if self.left: return self.left.height
      return -1


class BST:
    def __init__(self):
      self.root = None
      self.size = 0

    def __iter__(self):
      return self.root.__iter__()

    def __str__(self):
      return " - ".join(str(k) for k in self)

    def __contains__(self, key):
      return self.search(key) != None

    def preorder(self, v):
      if v:
        print(v, end=" ")
        self.preorder(v.left)
        self.preorder(v.right)

    def inorder(self,v):
      if v:
        self.inorder(v.left)
        print(v,end=' ')
        self.inorder(v.right)

    def postorder(self,v):
      if v:
        self.postorder(v.left)
        self.postorder(v.right)
        print(v, end=' ')
	
    def search(self, key):
      p = self.find_loc(key)
      if p and p.key == key:
        return p
      else:
        return None

    def find_loc(self, key):
      if self.size == 0:
        return None
      p = None
      v = self.root
      while v:
        if v.key == key:
          return v
        else:
          if v.key < key:
            p = v
            v = v.right
          else:
            p = v
            v = v.left
      return p

    def insert(self, key):
      p = self.find_loc(key)
      if p == None or p.key != key:
        v = Node(key)
        if p == None:
          self.root = v
        else:
          v.parent = p
          if p.key < key:
            p.right = v
          else:
            p.left = v
        self.size += 1
        self._update_height(v)
        return v
      else:
        return p
	
    def deleteByMerging(self,x):
      if x == None:
        return None
      a,b,pt = x.left, x.right, x.parent
      if a == None:
        c = b
        s = pt
      else:
        c = m = a
        while m.right:
          m = m.right
        m.right = b
        if b:
          b.parent = m
        s = m
      if self.root == x:
        if c:
          c.parent = None
        self.root = c
      else:
        if pt.left == x:
          pt.left = c
        else:
          pt.right = c
        if c:
          c.parent = pt
      del x
      self.size -= 1
      self._update_height(s)
      return s

    def deleteByCopying(self,x):
        if x == None:
          return None
        a = x.left
        if a == None:
          b, pt = x.right, x.parent
          if pt == None:
            self.root = b
          else:
            if pt.left == x:
              pt.left = b
            else:
              pt.right = b
          if b:
            b.parent = pt
          del x
        else:
          m = a
          while m.right:
            m = m.right
          x.key = m.key
          l, pt = m.left, m.parent
          if pt.left == m:
            pt.left = l
          else:
            pt.right = l
          if l:
            l.parent = pt
          del m
        self.size -= 1
        self._update_height(pt)
        return pt
	
	
    def height(self, x):
      if x == None:
        return -1
      return x.height

    def _update_height(self,v):
      while v != None:
        l, r = -1, -1
        if v.left :
          l = v.left.height
        if v.right:
          r = v.right.height
        v.height = max(l,r)+1
        v = v.parent

    def rotateLeft(self,x):
      z = x.right
      if z == None:
        return
      b = z.left
      z.parent = x.parent
      if x.parent:
        if x.parent.left == x:
          x.parent.left = z
        if x.parent.right == x:
          x.parent.right = z
      if z:
        z.left = x
      x.parent = z
      x.right = b
      if b:
        b.parent = x
      if self.root == x and z != None:
        self.root = z
      self._update_height(x)

    def rotateRight(self,z):
      x = z.left
      if x == None:
        return
      b = x.right
      x.parent = z.parent
      if z.parent:
        if z.parent.left == z:
          z.parent.left = x
        if z.parent.right == z:
          z.parent.right = x
      if x:
        x.right = z
      z.parent = x
      z.left = b
      if b:
        b.parent = z
      if self.root == z and x != None:
        self.root = x
      self._update_height(z)

      
    def succ(self, x):
      if x == None or self.size == 1:
        return None
      r = x.right
      while r and r.left:
        r = r.left
      if r:
        return r
      else:
        pr = x.parent
        while pr and pr.right == x:
          x = pr
          pr = pr.parent
        return pr
	
    def pred(self, x):
      if x == None or self.size == 1:
        return None
      r = x.left
      while r and r.right:
        r = r.right
      if r :
        return r
      else:
        pr = x.parent
        while pr and pr.left == x:
          x = pr
          pr = x.parent
        return pr
    
      
      
 class splayTree(BST):

    def splay(self, v):
        while v and v.parent != None:
          p = v.parent
          if p.parent == None:
            if p.left == v:
              self.rotateRight(p)
            else:
              self.rotateLeft(p)
          else:
            pp = p.parent
            if p.left == v and pp.left == p:
              self.rotateRight(p)
              self.rotateRight(v.parent)
            elif p.right == v and pp.right == p:
              self.rotateLeft(p)
              self.rotateLeft(v.parent)
            elif p.left == v and pp.right == p:
              self.rotateRight(p)
              self.rotateLeft(v.parent)
            else:
              self.rotateLeft(p)
              self.rotateRight(v.parent)
        return v

    def search(self, key):
        v = super(splayTree,self).search(key)
        if v:
          self.root = self.splay(v)
        return v

    def insert(self, key):
        v = super(splayTree,self).insert(key)
        if v:
          self.root = self.splay(v)
        return v

    def delete(self, x):
        if x == None: return
        self.splay(x)
        L, R = x.left, x.right
        m = L
        while m and m.right:
          m = m.right
        if m:
          L.parent = None
          self.root = self.splay(m)
          m.right = R
          if R: R.parent = m
          self._update_height(m)
        else:
          self.root = R
          if R: R.parent = None
            
            
T = splayTree()
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
