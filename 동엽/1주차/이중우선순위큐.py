import heapq

test_case = int(input())
for i in range(test_case):
    n = int(input())
    heap = []
    for k in range(n):
        command,number = input().split()
        if command == 'I':
            heapq.heappush(heap,int(number))
        else:
            if len(heap)==0:
                continue
            if number == "-1":
                # heapq.heapify(heap)
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
    if len(heap)==0:
        print('EMPTY')
    else:
        print(max(heap),heap[0])