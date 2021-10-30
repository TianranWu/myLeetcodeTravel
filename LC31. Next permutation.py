class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i >= 0:
            j = n-1
            while nums[i] >= nums[j] and j>=i:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        
        rev_left = i+1
        rev_right = n-1
        while(rev_left < rev_right):
            nums[rev_left],nums[rev_right] = nums[rev_right],nums[rev_left]
           
            rev_left+=1 
            rev_right-=1
            
            
 class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        left = None
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                left = i-1
                break

        if left is None:
            rev_left = 0
            rev_right = n-1
        else:
            right = n-1
            for i in range(left+1,n):
                if nums[i] > nums[left]:
                    right = i

            nums[left],nums[right] = nums[right],nums[left]
            rev_left = left+1
            rev_right = n-1

        while(rev_left < rev_right):
            nums[rev_left],nums[rev_right] = nums[rev_right],nums[rev_left]
            rev_left+=1 
            rev_right-=1

        
            
                
        
        
        
        
