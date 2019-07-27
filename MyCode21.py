# Bubble Sorting
## def sort(nums):
##     for i in range(len(nums)-1,0,-1):   # check the number of elements
##         for j in range(i):              # determine to swap or not
##             if nums[j] > nums[j+1]:
##                 temp = nums[j+1]
##                 nums[j+1] = nums[j]
##                 nums[j] = temp

# Selection Sorting
def sort(nums):
    for i in range(len(nums)):          # check the number of elements for sorting
        minpos = i
        for j in range(i,len(nums)):    # moving the sorting windows
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums [i] = nums[minpos]
        nums[minpos] = temp

nums = [5,3,8,6,7,2]
sort(nums)
print(nums)

