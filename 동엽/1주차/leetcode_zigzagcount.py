# 굳이 예제에 나온거처럼 공백을 표기해줄 필요가없다.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        graph = [[] for _ in range(numRows)]
        zig_count = 0
        row_count = 0
        last_col_point = 0
        flag = True
        answer = ""
        for i in s:
            if numRows == 1:
                graph[zig_count].append(i)
            else:
                if flag:
                    graph[zig_count].append(i)
                else:
                    # for _ in range(1,zig_count - last_col_point):
                    #     graph[zig_count].append(" ")
                    graph[zig_count].append(i)
                if zig_count == numRows-1:
                    flag = False
                if zig_count == 0:
                    flag = True
                    last_col_point = zig_count
                if flag:
                    zig_count+=1
                else:
                    zig_count -=1
                    row_count +=1
        for i in graph:
            answer+="".join(i)
        return answer