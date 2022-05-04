class Browser:
	def __init__(self):
		self.loc = 0 # 현재 무슨 페이지에 있는지 가르키는 변수
		self.log = [0]# 갔던 페이지거 몇번째 페이지 인지 순서대로 저장
		self.index = 0#몇번째 페이지에 있는지 나타냄
		self.List = ['www.hufs.ac.kr']#사이트 주소 저장 
		self.HList = []#history 출력을 위한 리스트
		print(self.List[0])
		
		
	def go(self, w):
		self.List.append(w)#페이지를 리스트에 append
		self.index = len(self.List) - 1 #go를 하면 가장 마지막 순서
		self.log = self.log[0:self.loc+1] #이 전 페이지까지 slicing하여 backward후 go에 대한 예외를 없앰
		self.log.append(self.index)# log에 이번 페이지가 몇번째 페이지 인지 저장
		self.loc += 1
		print(self.List[self.log[self.loc]])
	
	def forward(self):
		if self.loc != len(self.log) - 1:#가장 마지막 페이지면 forward못함
			self.loc += 1# 다음 페이지로 이동
			print(self.List[self.log[self.loc]])
			
	def backward(self):
		if self.loc != 0:# 첫 페이지면 backward못함
			self.loc -= 1# 이전 페이지로 이동
			print(self.List[self.log[self.loc]])
			
	def history(self):
		for value in self.List: 
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