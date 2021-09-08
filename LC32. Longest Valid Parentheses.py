# 方法二：栈
# 思路和算法

# 撇开方法一提及的动态规划方法，相信大多数人对于这题的第一直觉是找到每个可能的子串后判断它的有效性，但这样的时间复杂度会达到 O(n^3)O(n 
# 3
#  )，无法通过所有测试用例。但是通过栈，我们可以在遍历给定字符串的过程中去判断到目前为止扫描的子串的有效性，同时能得到最长有效括号的长度。

# 具体做法是我们始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」，这样的做法主要是考虑了边界条件的处理，栈里其他元素维护左括号的下标：

# 对于遇到的每个 \text{‘(’}‘(’ ，我们将它的下标放入栈中
# 对于遇到的每个 \text{‘)’}‘)’ ，我们先弹出栈顶元素表示匹配了当前右括号：
# 如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新我们之前提到的「最后一个没有被匹配的右括号的下标」
# 如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括号的长度」
# 我们从前往后遍历字符串并更新答案即可。

# 需要注意的是，如果一开始栈为空，第一个字符为左括号的时候我们会将其放入栈中，这样就不满足提及的「最后一个没有被匹配的右括号的下标」，为了保持统一，我们在一开始的时候往栈中放入一个值为 -1−1 的元素。




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
