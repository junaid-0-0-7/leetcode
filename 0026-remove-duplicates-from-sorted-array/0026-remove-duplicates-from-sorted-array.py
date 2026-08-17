class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        array = [] #create a empty array

        for i in range(len(nums)): #to get the index value and not the element itself for i
            if i == 0 or nums[i] != nums[i-1]: #take first number then compare the next number with previous one
                array.append(nums[i]) #store the number in array
        for i in range(len(array)): #this step is only for leetcode because it eants us to change nums its seld and nums = array will work but wont be accepted in leetcode
            nums[i] = array[i]
        return len(array) #returns the length


            