def maxArea(height):
    area, left, right = 0, 0, len(height)-1
    while left<right:
        area = max(area, min(height[left], height[right])*(right-left))
        left, right = (left+1, right) if height[left]<height[right] else (left, right-1)
    return area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))