import os
from functools import reduce

def getInput(filename):
    input_file = os.path.join(os.getcwd(), filename)
    fHandle = open(input_file, 'r')
    return fHandle.readlines()

def getNextline(line,total):
    nextLine = []  

    for x in range(len(line)-1):       
        nextLine.append(line[x+1]-line[x])       
 #   print(nextLine)
    if all(i == 0 for i in nextLine):
        return total
    return getNextline(nextLine, total+nextLine[-1])
    



def solve():
    lines = getInput('input9.txt')
    print(lines[0][:1])
    result = 0
    for line in lines:
        line= line.strip().split(' ')        
        line = [int(x) for x in line]
        value = getNextline(line,line[-1])
        #print(value)
        result +=value
    print(result)

def solve2():
    lines = getInput('input9.txt')
    print(lines[0][:1])
    result = 0
    for line in lines[::-1]:
        line= line.strip().split(' ')        
        line = [int(x) for x in line]
        value = getNextline(line,line[-1])
        #print(value)
        result +=value
    print(result)


if __name__ == "__main__":  
    solve()
    solve2()
