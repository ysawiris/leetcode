"""
Problem: Remove Duplicates from Sorted Array
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
   
   Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:
    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.

"""


"""
Restating the problem: 
    Traverse through a sorted array and remove all the duplicate values and return the new length

Ask Clarifying Questions:
    Do you want us to permentately delete duplicates from the sorted array? 
    Can we use a histogram/dictionary?
    Do you want us to return the new list a well?

State your assumptions: 
    We can assume that they dont want us to delete the duplicates from the sorted array. We can assume they just want us to count the     length of the array and exclude duplicate values from the count. We can assume that they don't want to allocate extra space for       another array, and we must do this by modifying the input array in-place with O(1) extra memory.

Think out loud: 
    Brainstorm solutions: 
        Brute Force: 
            Declare a histogram 
            Traverse through the array and add each number in to the histogram. If the number is already in the histogram add 1 to               its count. Return the length of keys in the histogram. 
        Solution: 
            Traverse through the array, you can check indexes at a time and see if they are equal to each other, if so then you have             found a duplicate. Now contuniue traversing untill you have reached a index where the its no longer a duplciate. Then                 exlcude them expect one.  

        
    Explain your rationale
    Discuss tradeoffs
    Suggest improvements:
        The brute force will work but they asked us not the allocate extra space for a new array. Therefore we are going to have a           counter and only add to the counter if the array[i] and array[i+1] are not equal to each other. This way we are able to find         the length of the array while only traverse once. Since the array is sorted we able to do this. 
"""



def removeDuplicates(nums):
    #
    length = 0 
    count = 0 

    curr_index = 0 
    

    while count < len(nums):
        print("Count: ", count)
        print("length: ", length)
        
        next_index = curr_index + 1 
        
        if nums[curr_index] == nums[next_index]: 
            print(nums[curr_index], nums[next_index])
            curr_index += 1
            count += 1
        else:
            curr_index += 1
            count += 1
            length += 1
    
    print("length: " + length)


if __name__ == "__main__":
    nums = [2,2,2,2,3,4,5,6,7]

    removeDuplicates(nums)