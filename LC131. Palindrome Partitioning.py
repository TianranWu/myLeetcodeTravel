# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(string, low, high):
            while low < high:
                if string[low] != string[high]:
                    return False
            return True
        
        def dfs(result, s, start, curList, dp):
            # print(dp)
            if start >= len(s):
                # print(curList)
                result.append(curList[:])
            
            
            for end in range(start,len(s)):
                if s[start] == s[end] and (end - start <= 2 or dp[start+1][end-1]):
                    # print(start,end)
                    # print(dp[start][end])
                    dp[start][end] = True
                    
                    curList.append(s[start: end+1])
                    dfs(result, s, end+1, curList, dp)
                    curList.pop()
        
        result = []
        curList=[]
        length = len(s)
        dp = [[False] * (length+1) for _ in range(length+1)]
        dfs(result, s, 0, curList, dp)
        
        return result
