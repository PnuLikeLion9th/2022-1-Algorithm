preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def dfs(start,end):
    if start>end:#더이상 자식 노드 없을때
        return
    root = preorder[start]
    idx = start+1

    while idx<=end:
        if preorder[idx]>root:
            break
        idx+=1
    dfs(start+1,idx-1)
    dfs(idx,end)
    print(root)

dfs(0,len(preorder)-1)


