class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        array = []      #create a new array to only store the elements that are not the value

        for i in range(len(nums)):       #go through every element in list
            if nums[i] != val:           #logic to check if element and value are same or not
                array.append(nums[i])    #use append to insert the element which is not 
        length = len(array)
        nums[:] = array                  #we use [:] to change the actual contents of nums as nums = array doesnt work since it will only change it in function
        return length


            