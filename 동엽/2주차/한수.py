#if suggested number has arithmetic sequence, we call it 한수

n = int(input())
answer = 0
for i in range(1,n+1):
    if i<100:
        answer +=1
    else:
        check = str(i)
        if int(check[2])-int(check[1]) == int(check[1])-int(check[0]):
            answer +=1
print(answer)