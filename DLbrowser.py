class DNode: # 이중연결리스트 노드
	def __init__(self, e):
		self.data = e
		self.next = None
		self.back = None
		
class DLinkedList: # 이중연결리스트
	def __init__(self):
		self.head = None
		self.tale = self.head
	
	def isEmpty(self):#연결리스틀가 비어 있는지 판별
		return self.head == None
	
	def size(self):#연결리스트의 크기
		count = 0#크기를 넣을 변수
		current = self.head #현재 위치 
		while current != None:
			count += 1#현재 위치에서 노드 하나 이동 할때 마다 count ++
			current = current.next
		
		return count
	
	def getNode(self, pos):#pos번째 노드를 구하는 멤버함수
		if pos < 0 : #pos < 0면 잘못된 pos
			return None
		node = self.head
		while pos > 0 and node != None:
			node = node.next
			pos -= 1
		return node
	
	def getEntry(self, pos):#pos번째 값 구하기
		node = self.getNode(pos)#pos번째 노드의 data값을 return
		if node == None:
			return None
		else:
			return node.data
	
	def append(self, data):
		if self.head == None:#리스트가 비어있다면 
			self.head = DNode(data)
			self.tail = self.head
		else:#비어있지 않다면
			node = self.tail
			new_node = DNode(data)
			new_node.back = node
			node.next = new_node
			self.tail = new_node
			
	def slicing(self,pos1,pos2):#원하는 인덱스 부분을 slicing
		Hnode = self.getNode(pos1)#pos1 ~ pos2부분 slicing
		Tnode = self.getNode(pos2)
		self.head = Hnode
		Tnode.next = None
		self.tail = Tnode
			
	
class Browser:
	def __init__(self):
		self.loc = 0 # 현재 무슨 페이지에 있는지 가르키는 변수
		self.log = DLinkedList()
		self.log.append(0)
		self.index = 0#몇번째 페이지에 있는지 나타냄
		self.List = DLinkedList()#사이트 주소 저장
		self.List.append('www.hufs.ac.kr')# 초기 사이트 주소 append
		self.HList = []#history 출력을 위한 리스트
		print(self.List.getEntry(0))
		
		
	def go(self, w):
		self.List.append(w)#페이지를 리스트에 append
		self.index = self.List.size() - 1#go를 하면 가장 마지막 순서
		self.log.slicing(0,self.loc) #이 전 페이지까지 slicing하여 backward후 go에 대한 예외를 없앰
		self.log.append(self.index)# log에 이번 페이지가 몇번째 페이지 인지 저장
		self.loc += 1
		print(self.List.getEntry(self.log.getEntry(self.loc)))
	
	def forward(self):
		if self.loc != self.log.size() - 1:#가장 마지막 페이지면 forward못함
			self.loc += 1# 다음 페이지로 이동
			print(self.List.getEntry(self.log.getEntry(self.loc)))
			
	def backward(self):
		if self.loc != 0:# 첫 페이지면 backward못함
			self.loc -= 1# 이전 페이지로 이동
			print(self.List.getEntry(self.log.getEntry(self.loc)))
			
	def history(self):
		for i in range(self.List.size()): 
			value = self.List.getEntry(i)
			if value not in self.HList: #중복이 안된다면 history에 append
				self.HList.append(value)
			else:# 중복이 된다면 삭제해준 후 다시 append하여 가장 최근에 들어간 페이지만 저장
				self.HList.remove(value)
				self.HList.append(value)
		for i in range(len(self.HList)):
			print(list(reversed(self.HList))[i])#reversed를 이용하여 반대로 출력
			
	def quit(self):
		return 0
		
bro = Browser()
esc = 1#종료를 위한 변수
while esc == 1:
	web = input().split()# 명령어와 사이트 주소를 나눠서 입력

	if web[0] == 'go':
		bro.go(web[1])
	
	elif web[0] == 'forward':
		bro.forward()
	
	elif web[0] == 'backward':
		bro.backward()
	
	elif web[0] == 'history':
		bro.history()
		
	elif web[0] == 'quit':
		esc = bro.quit()

