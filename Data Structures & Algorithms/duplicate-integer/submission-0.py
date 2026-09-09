class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_dict = {}
        for i in nums:
            if i not in new_dict:
                new_dict[i] = 1
            else:
                return True

        return False
                
