# myLeetcodeTravel


## My Notes

### 动态规划专题
Created 2021.05.24
Updated 2021.0524

### 664. Strange Printer
### 1035. 不相交的线
### 1143. 最长公共子序列


### LC819

这题用到了lambda function

`sort_result = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))`

### LC 11
动态规划以及优化速度的方法（把比较和计算复用起来，放到后面去，每次循环都省一次计算）

### LC5 longest palindromic substring
动态规划

## 速度问题review
### LC3 longest substring without repeating characters
滑动窗口法
```
我的方法是：
1. 统计字符串里的所有不同字符。用set函数即可实现。
2. maxlen = set的length，对当前maxlen：
    从0位置开始遍历字符串，看字符串里里有无最长为maxlen的不含相同char的子串
    如果有：maxlen --；无，break
3. return maxlen
```

i是截至j，以j为最后一个元素的最长不重复子串的起始位置，即索引范围是[i,j]的子串是以索引j为最后一个元素的最长子串。 当索引从j-1增加到j时，原来的子串[i,j-1]新增了一个元素变为[i,j]，需要判断j是否与[i,j-1]中元素有重复。所以if s[j] in st:是判断s[j]相同元素上次出现的位置，和i孰大孰小。如果i大，说明[i,j-1]中没有与s[j]相同的元素，起始位置仍取i；如果i小，则在[i,j-1]中有了与s[j]相同的元素，所以起始位置变为st[s[j]]+1，即[st[sj]+1,j]。而省略掉的else部分，由于s[j]是第一次出现所以前面必然没有重复的，仍然用i作为起始位置即可。 后面的ans=max(ans,j-i+1)中，括号中前者ans是前j-1个元素最长子串长度，j-i+1是以s[j]结尾的最长子串长度，两者（最长子串要么不包括j，要么包括j）取最大即可更新ans，遍历所有i后得到整个输入的最长子串长度。 不知道这样说是否清楚，望批评指正。


    
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

0422
- LC9

0423
- LC 12 Integer to Roman
执行用时：52 ms, 在所有 Python 提交中击败了81.21%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了41.66%的用户

0424
- LC 13
执行用时：68 ms, 在所有 Python 提交中击败了52.99%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了47.51%的用户
