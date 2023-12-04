import os
import re
def solve():
    input_filename = 'input4.txt'
    input_file = os.path.join(os.getcwd(), input_filename)

    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    answer = 0
    for line in lines:
       wincount = 0
       line = line.strip()
       cardNo = line.split(':')[0]
       card = line.split(':')[1]
       winners = card.split('|')[0].strip().split(' ')
       numbers = card.split('|')[1].strip().split(' ')
       iwinners = [int(w) for w in winners if w.isnumeric()]
       for n in numbers:
         if (n.strip().isnumeric()):
           ni = int(n.strip())
           if ni in iwinners:
             wincount+=1
#       print(cardNo, wincount)
       if wincount > 0:
         answer += pow(2,wincount-1)
    print(answer)

def solve2():
    input_filename = 'input4.txt'
    input_file = os.path.join(os.getcwd(), input_filename)

    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    answer = 0
    toCheck = [int(re.search('\d+',x.split(':')[0]).group()) for x in lines]
    wincountDict = {}
    for t in toCheck:
       line = lines[t-1]
       card = line.split(':')[1]
       winners = card.split('|')[0].strip().split(' ')
       numbers = card.split('|')[1].strip().split(' ')
       iwinners = [int(w) for w in winners if w.isnumeric()]
       wincount = 0
       for n in numbers:
         if (n.strip().isnumeric()):
           ni = int(n.strip())
           if ni in iwinners:
             wincount+=1
         wincountDict[t]=wincount

    t = 0
    while True and t < 14000000:
      if t >= len(toCheck):
        break
      if not toCheck[t] in wincountDict:
        break
      for i in range(1,wincountDict[toCheck[t]]+1):
        if toCheck[t]+i < len(lines)+1:
          toCheck.append(toCheck[t]+i)
      t+=1
    print(len(toCheck))
    print(t)
if __name__ == "__main__":
    solve()
    solve2()
