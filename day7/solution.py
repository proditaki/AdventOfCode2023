###
#Five of a kind, where all five cards have the same label: AAAAA
#Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#High card, where all cards' labels are distinct: 23456
###

import os
import re
import math

def solve():
    scores= []
    result = 0
    input_filename = 'input7.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    for line in lines:
        line = line.strip()
        cards, score = line.split(' ')
        score = int(score)
#        print(cards, score)
        if re.search(r'(.)\1{4}',cards):
            scores.append([7,cards.replace('A','E').replace('Q','C').replace('K','D').replace('J','B').replace('T','A'),score])
            #print('5', cards)
        elif re.findall(r'(.)\1{3}',"".join(sorted(cards))):
            #print('4', cards)
            scores.append([6,cards.replace('A','E').replace('Q','C').replace('K','D').replace('J','B').replace('T','A'),score])
        elif re.search( r'(?=.*(.)\1{2})(?=.*(?!\1)(.)\2{1})',"".join(sorted(cards))):
            #print('fh', cards)
            scores.append([5,cards.replace('A','E').replace('Q','C').replace('K','D').replace('J','B').replace('T','A'),score])
        elif re.findall(r'(.)\1{2}',"".join(sorted(cards))):
            #print('3', cards)
            scores.append([4,cards.replace('A','E').replace('Q','C').replace('K','D').replace('J','B').replace('T','A'),score])
        elif re.search( r'(?=.*(.)\1{1})(?=.*(?!\1)(.)\2{1})',"".join(sorted(cards))):
            scores.append([3,cards.replace('A','E').replace('Q','C').replace('K','D').replace('J','B').replace('T','A'),score])
            #print('2p', cards)
        elif re.findall(r'(.)\1{1}',"".join(sorted(cards))):
            #print('1p', cards)
            scores.append([2,cards.replace('A','E').replace('Q','C').replace('K','D').replace('J','B').replace('T','A'),score])
        else:
            #print('hc', cards)
            scores.append([1,cards.replace('A','E').replace('Q','C').replace('K','D').replace('J','B').replace('T','A'),score])
    i =1
    scores = sorted(scores)
    for index,cards,score in scores:

        print(scores[i-1])
        result += (i*score)
        i+=1
    print(result)
def solve2():
    scores= []
    result = 0
    input_filename = 'input7.txt'
    input_file = os.path.join(os.getcwd(), input_filename)
    fHandle = open(input_file, 'r')
    lines = fHandle.readlines()
    for line in lines:
        line = line.strip()
        cards, score = line.split(' ')
        score = int(score)
#        print(cards, score)
        if re.search(r'(.)\1{4}',cards) or re.search(r'^([^X])\1+X+$',"".join(sorted(cards.replace('J','X')))) or re.search(r'^[^X]X+$',"".join(sorted(cards.replace('J','X')))):
            scores.append([7,cards.replace('A','E').replace('Q','C').replace('K','D').replace('T','A').replace('J','1'),score])
            #print('5', cards)
        elif re.findall(r'(.)\1{3}',"".join(sorted(cards))) or re.search(r'^([^X])\1+[^X]X+$',"".join(sorted(cards.replace('J','X')))) or re.search(r'^[^X]([^X])\1+X+$',"".join(sorted(cards.replace('J','X')))) or re.search(r'^.*XXX$',"".join(sorted(cards.replace('J','X')))):
            #print('4', cards)
            scores.append([6,cards.replace('A','E').replace('Q','C').replace('K','D').replace('T','A').replace('J','1'),score])
        elif re.search( r'(?=.*(.)\1{2})(?=.*(?!\1)(.)\2{1})',"".join(sorted(cards))) or re.search(r'^([^X])\1([^X])\2X$',"".join(sorted(cards.replace('J','X')))):
            #print('fh', cards)
            scores.append([5,cards.replace('A','E').replace('Q','C').replace('K','D').replace('T','A').replace('J','1'),score])
        elif re.findall(r'(.)\1{2}',"".join(sorted(cards))) or re.search(r'.*([^X])\1+.*X+$',"".join(sorted(cards.replace('J','X')))) or re.search(r'^.*XX$',"".join(sorted(cards.replace('J','X')))):
            #print('3', cards)
            scores.append([4,cards.replace('A','E').replace('Q','C').replace('K','D').replace('T','A').replace('J','1'),score])
        elif re.search( r'(?=.*(.)\1{1})(?=.*(?!\1)(.)\2{1})',"".join(sorted(cards))):
            scores.append([3,cards.replace('A','E').replace('Q','C').replace('K','D').replace('T','A').replace('J','1'),score])
            #print('2p', cards)
        elif re.findall(r'(.)\1{1}',"".join(sorted(cards))) or re.findall(r'.*X$',"".join(sorted(cards.replace('J','X')))):
            #print('1p', cards)
            scores.append([2,cards.replace('A','E').replace('Q','C').replace('K','D').replace('T','A').replace('J','1'),score])
        else:
            #print('hc', cards)
            scores.append([1,cards.replace('A','E').replace('Q','C').replace('K','D').replace('T','A').replace('J','1'),score])
    i =1
    scores = sorted(scores)
    for index,cards,score in scores:
        result += (i*score)
        i+=1

    print(result)

if __name__ == "__main__":  
    solve()
    solve2()
