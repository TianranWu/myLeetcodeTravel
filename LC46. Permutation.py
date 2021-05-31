# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                print('before',first, nums)
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
            
                print('after',first,nums)
        
        n = len(nums)
        res = []
        backtrack()
        return res

solu = Solution()
solu.permute([1,2,3])






