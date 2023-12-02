#only 12 red cubes, 13 green cubes, and 14 blue cubes
import re
import os

def solve():
    input_filename = 'input.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    sum = 0
    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    for line in lines:
      amounts = {}
      splitLine = line.split(':')
      puzzleNo = re.sub('[^0-9]+','',splitLine[0])
      for blocks in re.split(', |; ',splitLine[1].strip()):
        block = blocks.split(' ')
        if not block[1] in amounts:
          amounts[block[1]] = int(block[0])
        else:
          if amounts[block[1]] < int(block[0]):
            amounts[block[1]] = int(block[0])
      if amounts['red'] <= 12 and amounts['blue'] <= 14 and amounts['green'] <= 13:
        sum += int(puzzleNo)
    print(sum)

def solve2():
    input_filename = 'input.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    sum = 0
    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    for line in lines:
      amounts = {}
      splitLine = line.split(':')
      puzzleNo = re.sub('[^0-9]+','',splitLine[0])
      for blocks in re.split(', |; ',splitLine[1].strip()):
        block = blocks.split(' ')
        if not block[1] in amounts:
          amounts[block[1]] = int(block[0])
        else:
          if amounts[block[1]] < int(block[0]):
            amounts[block[1]] = int(block[0])
      sum += amounts['red'] * amounts['blue'] * amounts['green']
    print(sum)
    
def solve2b(): # alternate solution :)
    input_filename = 'input.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    sum = 0
    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    for line in lines:
      reds = re.findall(r' (\d+) red', line)
      reds = [int(red) for red in reds]
      blues = re.findall(r' (\d+) blue', line)
      blues = [int(blue) for blue in blues]
      greens = re.findall(r' (\d+) green', line)
      greens = [int(green) for green in greens]
      sum+=max(reds)*max(blues)*max(greens)
    print(sum)
if __name__ == "__main__":
    solve()
    solve2()
