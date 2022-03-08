#정수 배열에 연산을 하기 위해 만듬
# 뒤집기와 버리기가 있음
# 도저히 어디틀린지 모르겠네 33%에 ㅈ버그 걸림..
from os import sep
from collections import deque
def main():
    T = int(input())
    for i in range(T):
        orders = input()
        n = int(input())
        str_list = input()
        rev_counter = 0
        if n>0:
            type_list = str_list[1:-1].split(',')
        else:
            type_list = []
        flag = 0
        for order in orders:
            if order == "R":
                rev_counter+=1
            else:
                if len(type_list)<1:
                    print("error")
                    break
                else:
                    if rev_counter%2 == 1:
                        type_list.pop()
                    else:
                        type_list.pop(0)
        if flag !=1:
            if rev_counter%2==1:
                type_list.reverse()
                print("[",",".join(type_list),"]",sep="")
            else:
                print("[",",".join(type_list),"]",sep="")




if __name__ == "__main__":
    main()