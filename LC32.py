class Solution:
    def longestValidParentheses(self, s: str) -> int:
        continue_count = 0
        max_continue = 0
        wait_time = 0

        stack = list()

        for i in range(len(s)):
            if wait_time >= 2 and s[i] == ")":
                max_continue = max(continue_count, max_continue)
                continue_count = 0


            if stack == []:
                stack.append(s[i])
                wait_time += 1
                continue

            if stack[-1] == "(" and s[i] == ")":
                stack.pop()
                continue_count += 2
                max_continue = max(continue_count, max_continue)
                wait_time = 0
                continue

            if s[i] == ')':
                max_continue = max(continue_count, max_continue)
                wait_time = 0
                
               

            print(stack, max_continue, wait_time)

        return max_continue
