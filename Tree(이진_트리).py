class Node:
    def __init__(self,data, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data



class Tree:
    def pre(self, node):
        if node is None: # 마지막에 node가 없으면 아무런 값도 돌려주지 않음
            return
        # 먼저 출력하는 이유는 전위는 노드-> 왼 -> 오이기 때문에
        # 루트를 먼저 출력하기 위해서 
        print(node.data, end =" -> ") 

        #재귀함수
        self.pre(node.left) # 노드의 왼쪽 찾기
        self.pre(node.right) # 노드의 오른쪽 찾기

        return node.data  # self.pre의 data 값을 올려줌



    def inor(self, node):
        if node is None:
            return


        self.inor(node.left) # 왼쪽 노드가 없을 때까지 내려감

        # 출력문이 중간에 있는 이유는 중위는 왼->노드->오
        # 그렇기 때문에 왼쪽으로 계속 내려가서 마지막에 있는 data출력
        print(node.data, end =" -> ")
        self.inor(node.right)

        return node.data # self.inor에서 받은 걸 위로 전해준다


    def post(self, node):
        if node is None:
            return

        self.post(node.left)
        self.post(node.right)

        # 출력문이 마지막에 있는 이유는 후위는 왼->오->노드
        # 그렇기 때문에 왼쪽으로 먼저 내려가고 그 다음 반환값을 통해 오른쪽으로 내려감
        print(node.data, end =" -> ")

        return node.data # self.post에서 값을 돌려줌
    

#-------------트리 만듦----------------------
n1 = Node("A") # root

n2 = Node("B") 
n3 = Node("C")

n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n8 = Node("H")

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n5.right = n8
#----------------------------------------



tree = Tree() # Tree에 있는 함수를 쓰기 위해 선언

menu = input("전위(pre)/중위(in)/후위(post): ")

if menu == "in":
     tree.inor(n1)
     print(None)
elif menu == "post":
    tree.post(n1)
    print(None)
elif menu == "pre":
    tree.pre(n1)
    print(None)
else:
     print("종료\n")

