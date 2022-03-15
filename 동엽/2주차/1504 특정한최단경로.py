#무방향 그래프
#특정 정점에서 특정 정점으로 이동하는 최단거리
#단 주어진 정점을 반드시 거쳐서 가야한다
#다 익스트라 알고리즘의 핵심은 최단경로를 계속해서
#갱신하는 것이다.

import sys
import heapq
input = sys.stdin.readline
N,E = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
start = 1
for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
ma,mb = map(int,input().split())
def dijkstra(start,target):
    distance = [INF]*(N+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,node = heapq.heappop(q)
        if distance[node]<dist:
            continue
        for next in graph[node]:
            cost = distance[node]+next[1]
            if cost<distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
    return distance[target]

case1=dijkstra(1,ma)+dijkstra(ma,mb)+dijkstra(mb,N)
case2=dijkstra(1,mb)+dijkstra(mb,ma)+dijkstra(ma,N)
if case1>=INF and case2>=INF:
    print(-1)
else:
    print(min(case1,case2))
    

# for i in range(1,len(distance)):
#     if distance[i] == INF:
#         print('못가')
#     else:
#         print(distance[i])
#우선순위 큐
# import sys
# import heapq
# input = sys.stdin.readline
# n,m = map(int,input().split())
# start = int(input())
# INF = int(1e9)
# distance = [INF]*(n+1)
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist,node = heapq.heappop(q)
#         if distance[node]<dist:
#             continue
#         for next in graph[node]:
#             cost = distance[node]+next[1]

#             if cost<distance[next[0]]:
#                 cost = distance[next[0]]
#                 heapq.heappush(q,(cost,next[0]))
# dijkstra(start)

# for i in range(1,len(distance)):
#     if distance[i] == INF:
#         print('dont go')
#     else:
#         print(distance[i])

# #다익스트라 구현 순차탐색
# n,m = map(int,input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] *(n+1)
# distance = [Infinity] *(n+1)

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))

# def get_smallest_node():#최단거리 노드 반환
#     min_value = Infinity 
#     index = 0 
#     for i in range(1,n+1):
#         if not visited[i] and distance[i] < min_value:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for i in graph[start]:
#         distance[i[0]] = i[1]

#     for _ in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for next in graph[now]:
#             cost = distance[now] + next[1]
#             if cost < distance[next[0]]:
#                 distance[next[0]] = cost
# dijkstra(start)

# for i in range(1,n+1):
#     if distance[i] == Infinity:
#         print("'can't go")
#     else:
#         print(distance[i])

