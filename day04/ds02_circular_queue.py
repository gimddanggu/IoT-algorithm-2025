# ds02_circular_queue.py
# 원형 큐 구현


def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐가 꽉 찼습니다')
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었습니다.')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었습니다.')
        return None
    return queue[(front+1) % SIZE]

# 전역 변수 선언
SIZE = int(input('큐 크기를 입력하세요 > '))
queue = [None for i in range(SIZE)]
front = rear = 0

if __name__ == '__main__':

    while True:
        select = input('삽입(I)/ 추출(E)/ 확인(V)/ 종료(Q) > ').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('입력 데이터 > ')
            enQueue(data)
            print(f'큐 상태: {queue}')
            print(f'front: {front}, rear: {rear}')
        elif select == 'E':
            print(f'추출된 데이터: {deQueue()}')
            print(f'큐 상태: {queue}')
            print(f'front: {front}, rear: {rear}')

        elif select == 'V':
            print(f'확인된 데이터: {peek()}')
            print(f'큐 상태: {queue}')
            print(f'front: {front}, rear: {rear}')

        else:
            print('입력이 잘못되었습니다.')