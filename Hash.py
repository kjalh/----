class HashTable:
    def __init__(self):
        self.size = 7
        self.table = [None] * self.size
        self.cnt = 0

    def add(self, key, value):
        if self.cnt / self.size >= 0.7: # 70%프로가 차면 크기 키움
            back_table = self.table  # 테이블 크기 변경 전 백업
            self.size = self.size*2 + 1     # size 크기 키움
            self.table = [None] * self.size # table 크기 키움
            self.cnt = 0  # 개수를 0으로 초기화

            for i in back_table:    # 반복문으로 백업한 값들 넣기 위한 반복문
                if i:                   # None은 거르는 조건문
                    self.add(i[0], i[1])    # key랑 value 넣기

        # 제산함수 사용으로 방 번호 정하기 (소수, 홀수가 좋음)
        # 기본 내장함수며 hash()는 모든 데이터를 정수로 바꿈
        idx = hash(key) % self.size 


        # 충돌해결 Open Addressing의 선형 조사법
        # None이 아니면 실행
        while self.table[idx] != None:
            if self.table[idx] == key: # 중복 데이터 안 쌓이게 
                break
            idx = (idx + 1) % self.size # 다른 칸으로 이동 

        # 인덱스를 구했고 해당하는 곳에 None이면 
        # 배열이 하나씩 차기 때문에 +1
        if self.table[idx] == None:
            self.cnt += 1

        # 값을 넣는다. 수정할 때도 있으니 위 if문에서 밖으로 뻄
        self.table[idx] = (key, value)




    def search(self, key):
        idx = hash(key) % self.size # 제산함수를 통해 인덱스 구하기

        # 충돌 해결
        while self.table[idx] != None:
            if self.table[idx][0] == key:
                return self.table[idx][1] # key값이 같으면 바로 반환
            idx = (idx + 1) % self.size   # 다른 칸으로 이동
                
        return None # 데이터 없으면 None반환
    


h = HashTable()

# 데이터 추가
h.add("1", "나")
h.add("2", "다")
h.add("3", "졸")
h.add("4", "리")
h.add("5", "다") # 70프로가 넘어 리사이징이 일어남



while True:
    print("추가하는 건 안 넣음")
    a = input("1/2/3/4/5/0(종료): ")

    if a == "0":
        exit()

    print(h.search(a))