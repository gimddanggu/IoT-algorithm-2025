# ds05_binary_tree_practice.py

import os

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역 함수 선언 부분 
memory = []
root = None
fnameAry = []

forderName = 'C:\Program Files\Common Files'
for dirName, subDirList, fnames in os.walk(forderName):
    for fname in fnames:
        fnameAry.append(fname)

node = TreeNode()
node.data = fnameAry[0]
root = node
memory.append(node)

dupNameAry = []

for name in fnameAry[1:]:
    node = TreeNode()
    node.data = name
    
    current = root
    while True:
        if name == current.data:
            dupNameAry.append(name)
            break
        if name < current.data:
            if current.left == None:
                current.left = node
                memory.append(node)
                break;
            current = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break;
            
            current = current.right

dupNameAry = list(set(dupNameAry))

print(f'{forderName} 및 그 하위 디렉터리의 중복된 파일 목록 -->')
print(dupNameAry)