# a *10 +1
# a *2
a,goal = map(int,input().split())
answer = 0
def dfs(a,count):
    if a>goal:
        return
    elif a == goal:
        global answer
        if answer !=0 and answer>count:
            answer = count
        else:
            answer = count
        return 
    dfs(a*10+1,count+1)
    dfs(a*2,count+1)

dfs(a,0)
if answer == 0:
    print(-1)
else:
    print(answer+1)