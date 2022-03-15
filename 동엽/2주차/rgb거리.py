#rgb거리에는 집이 n개 있쪄염 뿌우!
#빨강,초록,파랑 중 하나의 색으로 칠해야 하며
#각각의 집을 칠할때 비용이 주어진다.

# 인접하는 집과 색이 같아서 안된다.
import sys
input = sys.stdin.readline

N = int(input())
cache = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):#이전 집에서 선택한 색 제외 한 색중 최소값 누적합산
    cache[i][0] += min(cache[i-1][1],cache[i-1][2])
    cache[i][1] += min(cache[i-1][0],cache[i-1][2])
    cache[i][2] += min(cache[i-1][0],cache[i-1][1])
print(min(cache[-1]))


