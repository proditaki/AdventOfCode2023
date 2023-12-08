import os
import math
def getInput(filename):
    input_file = os.path.join(os.getcwd(), filename)
    fHandle = open(input_file, 'r')
    return fHandle.readlines()


def solve():
    nodeList = {}
    input_lines = getInput('input8.txt')
    instructions = input_lines[0].strip()
    #print(instructions)
    for line in input_lines[2:]:
        line = line.strip()
        name,LR = line.split(' = ')
        leftNode, rightNode =  LR[1:-1].split(', ')
     #   print(name, leftNode, rightNode)
        nodeList[name] = {'L': leftNode, 'R': rightNode}
        #print(nodeList)
    curNode = nodeList['AAA']
    answer = 1
    
    found = False
    while not found:
        for instruction in instructions:
            if curNode[instruction] == 'ZZZ':
                found = True
                print(f'found ZZZ in {answer} steps in node: {curNode}')
                break
            curNode = nodeList[curNode[instruction]]
            answer += 1

def solve2():
    nodeList = {}
    input_lines = getInput('input8.txt')
    instructions = input_lines[0].strip()
    for line in input_lines[2:]:
        line = line.strip()
        name,LR = line.split(' = ')
        leftNode, rightNode =  LR[1:-1].split(', ')
     #   print(name, leftNode, rightNode)
        nodeList[name] = {'L': leftNode, 'R': rightNode}
        #print(nodeList)
    A_Nodes = [node for node in nodeList.keys() if node.endswith('A')]
    totalSteps = {}
    for i in range(len(A_Nodes)):
        totalSteps[i] = 0
    
    for i, node in enumerate(A_Nodes):       
        curNode = nodeList[node]
        #print(curNode)
        found = False
        answer = 1
        while not found:
            for instruction in instructions:
                if curNode[instruction].endswith('Z'):
                    found = True
                    totalSteps[i] = answer
                    break           
                curNode = nodeList[curNode[instruction]]
               
                answer += 1
    totAnswer = 1
    print(f'fastest to all Zs : {math.lcm(*totalSteps.values())}')
if __name__ == "__main__":  
    solve()
    solve2()
