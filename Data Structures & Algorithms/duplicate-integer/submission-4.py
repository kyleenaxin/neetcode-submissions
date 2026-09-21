class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        secondList = []
        result = False
        for i in range(len(nums)):
            if nums[i] in secondList:
                result = True
            else:
                secondList.append(nums[i])
        return result