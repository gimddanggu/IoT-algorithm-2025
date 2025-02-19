# ds02_dfs.py
# 그래프 깊이 우선 탐색

stack = []          # 스택
visitedAry = []     # 방문기록
G1 = None

# 그래프 클래스
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0]*(self.SIZE) for _ in range(self.SIZE)]
    
    def __str__(self):
        return f'{self.graph}'


## 메인코드
SIZE = 4
G1 = Graph(SIZE)
# 0: A, 1: B, 2: C, 3: D
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print(G1)

print('## DFS 시작!')

current = 0 # A
stack.append(current) # stack push(A)
visitedAry.append(current)
# 바로 출력이 아니라 visitedAry 에 방문 기록이 남는 형식이구나

while len(stack) != 0: # stack 길이가 0이 되면 모든 정점을 방문했다는 뜻
    next = None
    for vertex in range(SIZE):
        if G1.graph[current][vertex] == 1:  # 간선이 있다는 뜻
            if vertex in visitedAry: # 도착점이 이미 방문했으면
                continue;
            else:
                next = vertex # 다음 번 방문할 정점
                break;

    if next != None: # 다음 방문할 정점이 있으면
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문순서', end='->')
for i in visitedAry:
    print(chr(ord('A')+i), end=' ')
print()
print(ord('A')) # A의 ASCII코드값 출력
