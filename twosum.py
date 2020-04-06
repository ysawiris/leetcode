"""
Problem: Two Sum 
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

"""


"""
Restating the problem: 
    Look through a given array of integers and check which indexes add up to the given target.

Ask Clarifying Questions:
    Can we use the same index to add up to the specific target? 
    What would you like me to return if no indices add up to the specific target? 
    Is the array of integers sorted? 

State your assumptions: 
    We may assume that each input would have exactly one solution, so you may not use the same element twice. 
    We can assume that the array for now will contain the numbers needed 
    to add up to a the target, but its always a good practice to assume that 
    the array will not contain the numbers needed. We can also assume that the array is sort but its also
    a good practice to assume its not. 

Think out loud: 
    Brainstorm solutions: 
        Brute Force: 
            Have a variable to keep track of one index, then check the other indexes in the array to see if they add up to the target. 
        Solution: 
            Declare a dictionary
            Traverse through the array and look at 2 index at a time. 
            Check if the indexes add up to the target
            if not then check which number is needed to add up to the target 
            and check if that number is in the dictionary we created
            if not continue untill we find the right indexes. 
        
    Explain your rationale
    Discuss tradeoffs
    Suggest improvements:
        The brute force will work but it will take forever to find it. We are not saving the (indexes, numbers) anywhere to memory, 
        so we are forced to check for all possible solutions untill we find the right pair, and this is whats going                   
        to take forever. So we decided to save the index and the number to memory, so we come to a new index 
        we can immedaitate know if we have seen the number that will add to the target and quickly return the indexes. 
        Ways to improve this is look at two indexes at time to speed up the traverse time. 
"""
from typing import List


def twoSum(nums, target):
        i = 0 
        dict = {}
        
        while True:
            current = i
            next = i + 1

            print(nums[current] + nums[next])

            total = nums[current] + nums[next]
            if target == total:
                print((current , nums[current]), ((next), nums[next]))
                break
            if nums[current] in dict.keys():
                print(nums[current])
                if target == nums[current] + dict[nums[current]]:
                    print((current , nums[current]), (nums[current], dict[nums[current]]))
                    break

            if nums[next] in dict.keys():
                print(nums[next])
                if target == nums[next] + dict[nums[next]]:
                    print((current , nums[current]), ((next), nums[next]))
                    break
            
            else:
                dict[nums[current]] = current
                dict[nums[next]] = next
                current = current + 1
            



if __name__ == "__main__":
    num = [2,3,5,8,6]
    target = 9

    twoSum(num,target)