#there's a two options in AC lanuage
#first one is R(reverse) and second one is D(delete)
#you will receive the number of test case and receive
#commands to perform the ac lanuage

from collections import deque

test_case = int(input())
for i in range(test_case):
    commands = list(input())
    n = int(input())
    composition_factor = deque(input()[1:-1].split(','))
    if n == 0:
        composition_factor = deque()
    reverse_odd = False 
    flag = False
    for command in commands:
        if command == "R":
            reverse_odd = not reverse_odd
        if command == "D":
            if len(composition_factor)==0:
                flag = True
                break
            if reverse_odd:
                composition_factor.pop()
            else:
                composition_factor.popleft()
    if flag:
        print('error')
    else:
        if reverse_odd:
            composition_factor.reverse()
            print("["+",".join(composition_factor)+"]")
        else:
            print("["+",".join(composition_factor)+"]")
        
