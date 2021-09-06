# 回溯要明确DFS的三个要素，以及剪枝这两个部分。

# DFS部分：

# 状态：括号不断叠加后的字符串，可能需要参量辅助记录有几个左括号，几个右括号
# 子状态：每一层的可选状态，两个，左括号，右括号
# 结束态：左括号用完，右括号用完
# 剪枝部分：

# 添加右括号不得超过左括号的数目
# 左括号最多只有n个

class Solution:
    def generateParenthesis(self, n: int):
        

        def backtrack(result, n, left_num, right_num):
            if left_num == n and right_num == n:
                results.append("".join(result))

            else:
                for i in range(2):
                    if i == 0:
                        if left_num == n: continue
                        left_num += 1
                        result.append('(')
                        backtrack(result, n, left_num, right_num)
                        result.pop()
                        left_num -= 1

                    if i == 1:
                        if left_num == right_num: continue
                        right_num += 1
                        result.append(")")
                        backtrack(result,n,left_num,right_num)
                        result.pop()
                        right_num -= 1

        result = list()
        results = list()
        backtrack(result, n, 0, 0)
        return results

                        
               
                    
                
