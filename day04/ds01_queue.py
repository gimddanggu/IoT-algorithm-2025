# ds01_queue.py
# 큐 자료구조 구현

# 함수 선언
def isQueueFull():
    global SIZE, queue, front, rear
    # 1. 가장 일반적 로직
    # if rear == SIZE - 1: # 괄호 잘 안씀
    #     return True
    # else:
    #     return False

    # 2. 개선 로직
    # 
    if rear != SIZE -1: # 큐가 꽉 안찼을 때
        return False
    elif rear == SIZE -1 and front == -1:
        return True
    # 앞 공간이 비었을 경우 
    else: # 데이터 한 칸씩 이동 shift
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i] # 데이터앞 빈자리에 첫번째 데이터 옮김
            queue[i] = None

        front -= 1
        rear -= 1
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear: # 괄호 잘 안씀
        return True
    else:
        return False
    

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is Full!!')
    else:
        rear += 1
        queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty!!')
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        return queue[front+1]


# 초기화
SIZE = int(input('큐크기 입력 > '))
queue = [None for _ in range(SIZE)]
front = rear = -1


## 메인모듈
if __name__ == '__main__':
    print('메인시작!')
    while True:
        select = input('삽입(I)/ 추출(E)/ 확인(V)/ 종료(Q) > ').upper()
        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태: {queue}')
        
        elif select == 'E':
            data = deQueue()
            print(f'추출 데이터: {data}')
            print(f'큐 상태: {queue}')
        
        elif select == 'V':
            print(f'확인 데이터: {peek()}')
            print(f'큐 상태: {queue}')
        
        else:
            print('입력 오류')
        

