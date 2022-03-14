class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1,len(height)):
        #         can_height = min(height[i],height[j])
        #         if answer<can_height*(j-i):
        #             answer = can_height*(j-i)
        # return answer
        last = len(height)-1
        start = 0
        while start<last:
            chosen_height = height[start] if height[start]<height[last] else height[last]
            container = (last-start)*chosen_height
            
            if height[start]>height[last]:
                last -=1
            else:
                start +=1
            if answer<container:
                answer = container
        return answer
                