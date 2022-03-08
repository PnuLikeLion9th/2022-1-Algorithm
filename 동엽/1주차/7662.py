# #데이터를 삭제할때 연산 명령에 따라 우선순위가 높은 데이터
# #낮은 데이터를 삭제하는게 포인트

# #최종적으로 q에 저장된 데이터중 최댓값과 최솟값을 출력

# #인서트 명령이 들어올때마다 정렬?
from collections import deque
import sys

# def quick_sort(nums):
#     if len(nums) <=1:
#         return nums
    
#     pivot = len(nums)//2
#     front_arr,pivot_arr,back_arr = [],[],[]
#     for value in nums:
#         if value < nums[pivot]:
#             front_arr.append(value)
#         elif value>nums[pivot]:
#             back_arr.append(value)
#         else:
#             pivot_arr.append(value)
#     return quick_sort(front_arr)+quick_sort(pivot_arr)+quick_sort(back_arr)

# def solution():
#     T = int(input())
#     for i in range(T):
#         q = deque()
#         N = int(input())
#         for j in range(N):
#             order_type,n = input().split()
#             if order_type == "I":
#                 q.append(int(n))
#                 q = quick_sort(q)
#             else:
#                 if len(q)==0:
#                     continue
#                 else:
#                     if n == "1":
#                         q.pop()
#                     else:
#                         q.pop(0)
#         if len(q)==0:
#             print("EMPTY")
#         else:
#             print(q[-1],q[0])

# if __name__ == "__main__":
#     sys.setrecursionlimit(100000)
#     solution()

# 퀵소트 알고리즘 recursion 횟수 초과
# def solution():
#     T = int(input())
#     for i in range(T):
#         n = int(input())
#         array = list()
#         for j in range(n):
#             order,number = input().split()
#             if order == "I":
#                 array.append(int(number))
#                 array.sort()
#             else:
#                 if len(array)==0:
#                     continue
#                 else:
#                     if number == "1":
#                         array.pop()
#                     else:
#                         array.pop(0)
#         if len(array)==0:
#             print("EMPTY")
#         else:
#             print(array[-1],array[0])

# solution()

#리스트 정렬 시간초과

#3차 시도 병합정렬

# def merge_sort(nums):
#     if len(nums)<2:
#         return nums
#     mid = len(nums)//2
#     print(mid)
#     low_arr = merge_sort(nums[:mid])
#     high_arr = merge_sort(nums[mid:])
#     merged_arr = []
#     l=h=0
#     while l<len(low_arr) and h<len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l+=1
#         else:
#             merged_arr.append(high_arr[h])
#             h+=1
    
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr

import heapq

def solution():
    T = int(input())
    for i in range(T):
        n = int(input())
        array = list()
        for j in range(n):
            order,number = input().split()
            if order == "I":
                heapq.heappush(array,number)
            else:
                if len(array)==0:
                    continue
                else:
                    if number == "1":
                        array = heapq.nlargest(len(array),array)[1:]
                        print("continue",array)
                    else:
                        array.pop(0)

        if len(array)==0:
            print("EMPTY")
        else:
            print(array)
            print(array[-1],array[0])

solution()