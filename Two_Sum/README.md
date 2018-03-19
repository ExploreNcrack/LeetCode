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
<br />There are two different ways to think about it.
<br />The first one would be basically find the two numbers in the array that add up to the target
<br />The second one is that we can find the complement of the current number and see if the complement exists in the array that is given
