# myLeetcodeTravel


## My Notes

### 动态规划专题
Created 2021.05.24
Updated 2021.05.24


#### 5. 最大子回文串
    中心扩散方法，分类讨论：单数回文和双数回文——扩散中心不同
#### 664. Strange Printer
#### 1035. 不相交的线
#### 1143. 最长公共子序列

以二维的dp矩阵居多，通常以i和j来表示。

一定要分析清楚依赖关系，从而确定ij在循环中应该是递增还是递减。

### 搜索回溯专题


### 其他技巧问题
#### LC819

这题用到了lambda function

`sort_result = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))`

#### LC 11
动态规划以及优化速度的方法（把比较和计算复用起来，放到后面去，每次循环都省一次计算）

#### LC5 longest palindromic substring
动态规划

### 速度问题review
#### LC3 longest substring without repeating characters
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

#### LC4
#### LC1573


