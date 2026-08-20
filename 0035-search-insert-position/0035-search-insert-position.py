class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0          #counter
        for i in range(len(nums)):     #check the whole array
            if nums[i] == target:      #if current element is equal to target value
                count = i
            elif target >= nums[i]:    #since its a sorted array we are taking advantage of the fact that we can place the element after its lesser version and even if there are duplicates it wont matter
                count = i + 1
        return count

