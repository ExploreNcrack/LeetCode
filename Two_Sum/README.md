# Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

## From LeetCode
**Link**: https://leetcode.com/problems/two-sum/description/


## Example
Given nums = [2, 7, 11, 15], target = 9,
<br />Because nums[0] + nums[1] = 2 + 7 = 9,
<br />return [0, 1].

## Explanantion
The goal of this problem is to find the two numbers that add up to a specific target.
<br />
<br />There are **two different ways** to think about it.
<br />
### Method 1
<br />The first one is that we can loop through each number in the array and **find the complement(target-current_number) of the current number then check if the complement exists in the array that is given**. **Checking if the complement exists in the given array is a major factor that determines the time complexity**. We would like to reduce the time it takes to perform such check operations. A simple but efficient solution is to store the number as key and its index as value into a **dictionary**. Since the data is stored in a dictionary structure, **retrieve/check if a key exists in the dictionary takes only O(1) constant time**. Since complement comes in pair(If two nums in the array add up to the target, they must be complement to each other so as long as one of the complement is in the dictionary, scanning array once will guarantee that we will find them no matter in what condition) we can store num and its index into dictionary while checking if its complement exists in the dictionary. This will only result one traverse of the given array. 
<br />
<br />The time complexity for this method will be **O(n)**, n as the size of the given array, since we just need one scan of the array and each number only take **O(1)** to perform the check.

### Method 2
<br />The second one would be basically find the two numbers in the array that add up to the target by traversing each number in the array

