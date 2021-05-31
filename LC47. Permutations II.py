class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        res=[]
        ans=[]
        n=len(nums)
        visited=[0]*n
        def dfs():
            if len(ans)==n:
                res.append(ans[::])
            for i in range(n):
                if visited[i] or i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                ans.append(nums[i])
                visited[i]=1
                dfs()
                ans.pop()
                visited[i]=0
        dfs()
        return res