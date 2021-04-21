# myLeetcodeTravel
[toc]

## My Notes

### LC819

这题用到了lambda function

'sort_result = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))'

### LC 11
动态规划以及优化速度的方法（把比较和计算复用起来，放到后面去，每次循环都省一次计算）

### LC5 longest palindromic substring
动态规划

## 速度问题review
### LC3 
``` python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans;
```

### LC4
### LC1573

## Submit Records

### April 2021
0415

- LC1573
执行用时：436 ms, 在所有 Python3 提交中击败了6.25%的用户
内存消耗：31.4 MB, 在所有 Python3 提交中击败了5.21%的用户

- LC819
执行用时：40 ms, 在所有 Python3 提交中击败了85.25%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了14.41%的用户

0416

- LC1
在所有 Python 提交中击败了86%的用户
在所有 Python 提交中击败了44%的用户

- LC11
执行用时：172 ms, 在所有 Python 提交中击败了24.07%的用户
内存消耗：21 MB, 在所有 Python 提交中击败了45.58%的用户

0417

- LC3 
执行用时：388 ms, 在所有 Python3 提交中击败了14.22%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了7.00%的用户

- LC4 (第一个一次成功的！)
执行用时：64 ms, 在所有 Python3 提交中击败了23.08%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了11.61%的用户

0418

- LC5
不会做！

- LC6
不会做！

0420

- LC7
执行用时：24 ms, 在所有 Python 提交中击败了83.58%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了98.73%的用户


0421 

- LC8
执行用时：24 ms, 在所有 Python 提交中击败了93.84%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了94.72%的用户