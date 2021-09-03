class Solution(object):
    def swap(self, s, left, right):
            news = s[0:left]
            for i in range(right-1, left, -1):
                # print(i)
                news = news + s[i]
            news = news + s[right+1:]
            return news

    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        
        # return self.swap(s,1,4)
        news = s
        left = []
        right = []
        swap_count = 0

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)

            if s[i] == ')':
                right.append(i)
                right_count = sum([emt<left[-1] for emt in right]) 

                news = self.swap(news, left[-1] - 2 * right_count, i - 2*swap_count)
                swap_count+=1
                
                left = left[:-1]    
                print(swap_count, right_count)    
        
        return news

solu = Solution()
print(solu.reverseParentheses("(!ih)(ed(!ih)(et(oc))el)"))