import re
import os
from functools import reduce

def solve2():
    input_filename = 'input3.txt'
    input_file = os.path.join(os.getcwd(), input_filename)

    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    result = 0
    numMap = []
    for x in range(len(lines)):
      y = 0
      e = 0
      while True:
        nums = re.search('\d+', lines[x][e:])
        if not nums:
          break
        e += nums.end()
        b = e-nums.end()+nums.start()
        numMap.append((int(lines[x][b:e]),(x,b,e-1)))

    gears = {}
    for num in numMap:
      for x in range(num[1][0] - 1, num[1][0] + 2):
        if x >= 0 and x < len(lines):
          for y in range(num[1][1] - 1, num[1][2] + 2):
            if y >= 0 and y < len(lines[0]):
              if lines[x][y] == "*":
                if not gears.get((x, y)):
                  gears[(x, y)] = []
                gears[(x, y)].append(num[0])
    gear_ratios= 0
    for gear in gears:
      if len(gears[gear]) == 2:
        gear_ratios += gears[gear][0] * gears[gear][1]

    print(f'answer {gear_ratios}')


def solve():
    input_filename = 'input3.txt'
    input_file = os.path.join(os.getcwd(), input_filename)

    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    result = 0
    for i in range(len(lines)):
      line = lines[i].strip()

      e = 0
      while True:
        numbers = re.search('\d+', line[e:])
        if not numbers:
          break

        e += numbers.end()
        b = e-numbers.end()+numbers.start()
        if b > 0:
          if line[b-1] != '.':
            result += int(re.sub('[^0-9]+','', line[b:e]))
            continue
        if e < len(line):
          if(line[e] != '.'):
            result += int(re.sub('[^0-9]+','', line[b:e]))
            continue
        found = False
        if 1==1:
          if i != 0:
            for z in range (b-1 if b >0 else b,e+1 if e < len(line) else e):
              if lines[i-1][z] != '.': #chr(46)
                result += int(re.sub('[^0-9]+','', line[b:e]))
                found = True
                break
        if found: continue
        if  1==1:
          if i < len(lines)-1:
            for z in range (b-1 if b >0 else b,e+1 if e < len(line) else e):
              if lines[i+1][z] != '.':
                result += int(re.sub('[^0-9]+','', line[b:e]))
                break
    print(f'result {result}')
if __name__ == "__main__":
    solve()
    solve2()
