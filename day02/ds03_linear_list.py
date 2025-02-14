# ds03_linear_list.py
# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는 게 아님
# 배열 (선형리스트)가 어떻게 동작하는지 로직을 파악할 것!

## 전역변수 선언 부분
# 빈 배열 생성
katok = []
select = -1 # -1 통과, 1: 추가, 
# 데이터 마지막에 값 추가(append)
def list_add_data(friend):
    katok.append(None)
    lenKatok = len(katok)

    katok[lenKatok - 1] = friend

# 중간에 데이터 삽입(insert)
def list_insert_data(pos, friend):
    # 잘못된 인덱스를 넣었을 때 예외처리 필요
    if pos < 0 or pos > len(katok):
        print('실행범위를 벗어났습니다.')
        return
    katok.append(None)
    # 삽입할 위치
    
    lenKatok = len(katok)
    
    for i in range(lenKatok-1, pos, -1):
        # 끝에서 부터 한 칸씩 이동
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[pos] = friend

# 데이터 삭제(remove)
def list_remove_data(pos):
    # 예외처리: 인덱스 범위가 올바르지 않을 경우
    if pos < 0 or pos > len(katok):
        print('데이터 삭제 범위를 벗어났습니다.')
        return
    
    lenKatok = len(katok)
    katok[pos] = None # 지정된 위치 값을 삭제

    for i in range(pos+1, lenKatok):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[lenKatok - 1]) # 배열 맨 마지막 삭제


## 메인코드 영역
if __name__ == '__main__':

    while True:
        select = int(input('선택(1: 추가, 2: 삽입, 3: 삭제, 4: 종료) >'))
        
        if select == 1:
            data = input('추가할 데이터 입력> ')
            list_add_data(data)
            print(katok)

        elif select == 2:
            idx, ins_data = input('삽입 위치, 데이터 입력 --> ').split()
            list_insert_data(int(idx), ins_data)
            print(katok)

        elif select == 3:
            idx = int(input('데이터 삭제할 위치를 입력해주세요'))
            list_remove_data(idx)
            print(katok)
            
        elif select == 4:
            break;
        else:
            print('번호를 잘못 입력했습니다. 다시 입력해주세요(1 ~ 4)')


