def twoSum(nums, target):
    'solution2'

    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
   
    nums = [[num, i] for i,num in enumerate(nums)]
       
    nums.sort()
    sum = 0
    i, j = 0, len(nums) - 1
    while 1: 
        if (i==j):
            return
        sum = nums[i][0] + nums[j][0]
        if (sum < target): 
            i += 1
        elif (sum > target): 
            j -= 1
        else: 
            return [nums[i][1], nums[j][1]]

test = [3 ,1 ,8 ,9 ,11]
target = 20
output = twoSum(test, target)

print(test)

if output == None:
    print("No two numbers in the array can add up to target")
else:
    print("num: %d and %d can add up to target: %d"%(test[output[0]], test[output[1]], target))