def twoSum(nums, target):
    'solution1'

    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dictionary = {}
    for i, num in enumerate(nums):
        if target - num in dictionary:
            return [dictionary[target - num], i]
        dictionary[num] = i



test = [3 ,1 ,8 ,9 ,11]
target = 22
output = twoSum(test, target)

print(test)

if output == None:
    print("No two numbers in the array can add up to target")
else:
    print("num: %d and %d can add up to target: %d"%(test[output[0]], test[output[1]], target))
