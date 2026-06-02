class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
        



class LinkedList:
    def __init__(self):
        self.node ={}
        self.head = None
        self.node_cnt = 1
        pass

    def in_data(self):
        value = input("추가 값 입력:")
        
        # 딕셔너리 노드를 만듦
        self.node[self.node_cnt] = [value, None]
        
        if self.head == None: # head가 None이면 head 지정
            self.head = self.node_cnt 
            
        else:
            prev_next = self.node_cnt - 1 # 전에 만든 next값 생성  
            prev_value = self.node[prev_next][0] # 전에 만든 딕셔너리에 value값을 가져 옴
            
            # 전에 만든 딕셔너리에 전에 넣은 value를 다시 넣고 지금 만든 next값 넣기
            self.node[prev_next] = [prev_value, self.node_cnt]
    
        self.node_cnt += 1 # 다음 node를 위해 1증가

        return print(f"{self.node}") # 그냥 눈으로 확인
        
        

    def out_data(self):
        if self.head == None: # head가 None이면 값이 없다는 걸 의미
            return print("리스트 비어 있음")
        
        data = input("삭제할 값: ")
        
        next = self.head
        prev = None

        while next != None: # next가 None이면 멈춤
            if self.node[next][0] == data: # 삭제할 데이터가 같은지 호가인
                if prev == None:
                    self.head = self.node[next][1] # head를 다음 노드로 바꿈
                else:
                    self.node[prev][1] = self.node[next][1] # 다음 next를 이전 next로 바꿈
                

                del self.node[next] # 옮겼으니 해당 data 삭제
                print(f"{data} 삭제함")
                return print(f"{self.node}") # 확인
            
            prev = next  # next에 다음값 입력 전에 prev로 이전값 세팅
            next = self.node[next][1]  # 다음 값 입력

        print(f"{data}가 안에 없음")
        return print(f"{self.node}")



                    






    def find_data(self):
        if self.head == None:   # head가 None이면 값이 없다는 걸 의미
            return print("리스트 비어 있음")
        
        m = int(input("전체조회(1)/원하는 값 조회(2): ")) 
        
        
        if m == 1:
            next = self.head    # next에 head를 옮긴다 그냥 첫 시작
            
            i = 0
            while next != None: # None이 나오면 멈춤
                i+=1
                print(f"{i}번에 {self.node[next][0]}")

                next = self.node[next][1]   # 다음 값을 next에 저장

        elif m == 2:
            w = input("원하는 값: ")

            next = self.head

            i = 0
            while True:
                i += 1
                if next == None:  # 마지막까지 돌았다는 얘기
                    return print('원하는 값 없음')
                elif self.node[next][0] == w:  # 원하는 값 찾음
                    return print(f"원하는 값: {self.node[next][0]}은 {i}번째에 있음")
                
                else:  # 둘 다 아니면 next에 다음 값 입력
                    next = self.node[next][1]
              



lin = LinkedList()

while True:
    menu = input("apnd/del/find/0(종료) : ")

    if menu == "apnd":
        lin.in_data()
    elif menu == "del":
        lin.out_data()
    elif menu == "find":
        lin.find_data()
    elif menu == "0":
        exit()
    else:
        print("다시 입력")

