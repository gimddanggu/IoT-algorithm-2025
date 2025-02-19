# ds05_binary_tree_practice.py
## 중복파일 이름 찾기

# 특정폴더 지정해서 해당 폴더 및 그 하위 폴더에 모든 파일 조회
# 이름이 동일한 파일 있으면 그 이름을 출력
# 파일 경로
import os
# os.path.isfile() 파일인지 확인
# os.path.isdir()  폴더인지 확인ㄴ


class Tree:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


file_path = 'C:\Program Files\Common Files'
dir = os.listdir(file_path)


# 트리 생성
node = Tree()
for i in dir:
    if os.path.isdir(file_path + f'\{i}'):
        pass