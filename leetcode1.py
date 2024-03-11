# Give an an array of integers (nums) [1,2,3,4,5] and a integer (target).
# Return indices of the two numbers so that they add up to target
# Each input has only one solution, can't use same element twice.

#We look through the array

class Solution:
    def TwoSum(self, input: list[int], target: int):
        #loop through
        for index, item1 in enumerate(input):
            #take item as base, and loop trough remaining
            for sindex, item2 in enumerate(input):
                #if sindex = index continue
                if index == sindex: continue
                #equation adds up
                if item1 + item2 == target: 
                    return([index,sindex])

Sol = Solution()
input = [3,2,4]
target = 6
print(Sol.TwoSum(input,target))
