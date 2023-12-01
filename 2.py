import re
import os

def solve():
    input_filename = '1.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    written_numbers=['one','two','three','four','five','six','seven','eight','nine']

    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    sum=0

    for line in lines:
        firstdigit = re.search(r"(one|two|three|four|five|six|seven|eight|nine|[0-9])", line)[0]
        lastdigit = re.search(r"(enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|[0-9])", line[::-1])[0][::-1]

        if not (firstdigit.isdigit()):
            firstdigit = firstdigit.replace(firstdigit,str(written_numbers.index(firstdigit)+1))
        if not (lastdigit.isdigit()):
            lastdigit = lastdigit.replace(lastdigit,str(written_numbers.index(lastdigit)+1))
        cleanline = line.strip()
        print(f'{cleanline} {firstdigit} {lastdigit}')
        sum +=  int(f'{firstdigit}{lastdigit}')
    print(f'Answer: {sum}')
if __name__ == "__main__":
    solve()

