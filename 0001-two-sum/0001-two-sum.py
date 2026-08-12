class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            var = target - nums[i]  # target is subtract by the first variable and stored in var
            for j in range(len(nums)):
                if i!= j and var == nums[j]: # check the list where the variable matches var
                    return(i,j)
    