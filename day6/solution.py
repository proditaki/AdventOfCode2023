import os
import re
import math
def solve():
    input_filename = 'input6.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    times = lines[0].strip()
    records = lines[1].strip()
    times = re.split(' +', re.split(': +', times.strip())[1])
    records = re.split(' +', re.split(': +', records.strip())[1])
    result = 1
    for x in range(len(times)):
        result *= calcMaxDistance(int(times[x]),int(records[x]))
    print(result)

def calcMaxDistance(time, record):
    count = int(math.floor(time + math.sqrt(math.pow(time,2)-record*4))/2 -math.ceil(time - math.sqrt(math.pow(time,2)-record*4))/2) +1
    return count   
#old solution
#    retval = 0
#    for x in range(time):
#        if ((time-x)*x) >= record:
#            retval += 1
#
#    return retval

def solve2():
    input_filename = 'input6.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    times = lines[0].strip()
    records = lines[1].strip()
    times = re.sub(' ','',re.split(': +', times.strip())[1])
    records = re.sub(' ','',re.split(': +', records.strip())[1])        
    
    
    result = calcMaxDistance(int(times),int(records))
    print(result)

if __name__ == "__main__":  
    solve()
    solve2()
