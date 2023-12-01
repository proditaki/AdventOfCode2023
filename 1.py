import re
import os

def solve():
    input_filename = '1.txt'
    input_file = os.path.join(os.getcwd(), input_filename)

    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    sum=0
    i = 0
    for line in lines:
        cleanline = line.strip()
        cleanline = re.sub('[^0-9]', '',cleanline)
        firstNum = int(cleanline[0])*10
        lastNum = int(cleanline[-1])
        sum += firstNum+lastNum
        i +=1
    print(f'Answer: {sum}')
if __name__ == "__main__":
    solve()
