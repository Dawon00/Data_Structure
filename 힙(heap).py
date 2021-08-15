class Heap:
	def __init__(self, L=[]):
		self.A = L
	def __str__(self):
		return str(self.A)

	def heapify_down(self, k, n):
		while 2*k+1 <n:
			L, R = 2*k+1, 2*k+2
			if L<n and self.A[L] > self.A[k]: #본인 k와 자식 둘 중 큰 값
				m=L
			else:
				m=k
			if R < n and self.A[R] > self.A[m]:
				m = R
			if m != k:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				k=m
			else:
				break
	
	def make_heap(self):
		n = len(self.A)
		for k in range(n-1, -1, -1):
			self.heapify_down(k,n) #리프노드

	def heap_sort(self):
		n = len(self.A)	
		for k in range(len(self.A)-1, -1, -1):
			self.A[0],self.A[k] = self.A[k],self.A[0]
			n = n - 1	# A[n-1]은 정렬되었으므로
			self.heapify_down(0, n)

S = [int(x) for x in input().split()]
H = Heap(S) #부모가 자식보다 커야한다
H.make_heap() #힙성질에 맞게 조정
H.heap_sort() #리스트 오름차순으로 정렬
print(H)
