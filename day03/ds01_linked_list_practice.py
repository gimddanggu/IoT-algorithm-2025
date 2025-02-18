# 사용자가 이름, 이메일을 입력
# 이메일 순서대로 단순 연결 리스트를 생성
# 이름에서 enter를 입력하면 종로된다.
# 정보 입력하면 모든 정보 출력
# 전역변수
head, prev, curr = None, None, None

class Node:
    # __link = None

    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__link = None

    def setLink(self, link):
        self.__link = link
    
    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email
    
    def getLink(self):
        return self.__link
    
    def __str__(self):
        return f'{self.getName()}/{self.getEmail()}'



def printNode(start):
    curr = start
    if curr is None: return
    else:
        print(f"['{curr.getName()}', '{curr.getEmail()}']", end=' ')
        while curr.getLink() != None:
            curr = curr.getLink()
            print(f"['{curr.getName()}', '{curr.getEmail()}']", end=' ')

        print()

def insert_node(name, email):
    global head, curr
    node = Node(name, email)
    if head is None:
        head = node
    else:
        curr = head
        if curr.getEmail() > node.getEmail():
            node.setLink(head)
            head = node
            return
        # curr 를 바꿔주지 않아서 무한루프 발생했음
        while curr.getLink() is not None:
            if curr.getEmail() < node.getEmail() < curr.getLink().getEmail():
                node.setLink(curr.getLink())
                curr.setLink(node)
                return
            curr = curr.getLink() 
        curr.setLink(node)

if __name__ == '__main__':
    while True:
        name = input('이름   ----> ')
        if name == '':
            break
        email = input('이메일 ----> ')
        # printNode(head) # 노드 추가 후 바로 실행되는 게 보기 좋음
        
        insert_node(name,email)
        printNode(head)
        
        '''
        if head is None:
            node = Node(name, email)
            head = node

        # 값이 하나라도 있을 경우
        else:
            prev = head
            node = Node(name, email)
            while prev.getLink() != None:
                prev = prev.getLink()
                # if prev.getLink() == None:
                #     prev.setLink(node)
                #     print(1)
                # 기존 if 를 사용한 코드는 노드가 2개 이상 있을 때만 동작
            prev.setLink(node) # setter 정확하게 사용하기 setLink() = node (x) 
            '''
        
        


