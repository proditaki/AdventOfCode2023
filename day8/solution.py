import os

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
    pass

if __name__ == "__main__":  
    solve()
    solve2()
