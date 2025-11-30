def traped_water(height):
    total = 0
    left = 0
    right = len(height)-1
    leftmax = 0
    rightmax = 0
    while left < right:
        if height[left] <= height[right]:
            if leftmax > height[left]:
                total += leftmax - height[left]
            else:
                leftmax = height[left]
            left += 1
        else:
            if rightmax > height[right]:
                total += rightmax - height[right]
            else:
                rightmax = height[right]
            right -= 1
    return total

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(traped_water(height))