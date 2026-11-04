class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right=len(heights)-1          #[1,7,2,5,4,7,3,6]
        while left < right:
            height = min(heights[left], heights[right])         #1      #
            width = abs(left-right)              #5
            newArea = height * width             #5
            area = max(area, newArea)            #5
            if heights[left] < heights[right]:   #true
                left +=1                         #7
            else:
                right -=1
        return area