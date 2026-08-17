class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pointer = strs[0]     #pointer is the first word of string list

        for i in strs:        #i is going through every word in the list of string
            while not i.startswith(pointer):  #only erases last letter if the prefix is not there in whole word
                pointer = pointer[:-1]
        return pointer #after the prefix is found it is returned and next word is checked