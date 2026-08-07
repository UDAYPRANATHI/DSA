class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        result=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                result.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i]==0:
                    result.append(0)
        print(result)

        for i in range(len(nums)):
            nums[i] = result[i]