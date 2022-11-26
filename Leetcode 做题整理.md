[toc]

# 数据结构基础

- 常用的数据结构：队列、链表、栈、字典等依次介绍大致的实现逻辑与应用场景； 
- [哈希表]()的实现方法；介绍哈希，如何解决冲突，如何扩容，如何平滑扩容

# Leetcode 做题整理

- LRU

  - 初始化注意
  - def __init__(self, capacity):
            """
            :type capacity: int
            """
            self.cache = dict()
            self.size = 0
            self.capacity = capacity
            self.head = DLinkedList()
            self.tail = DLinkedList()
            self.head.next = self.tail
            self.tail.prev = self.head

- 1143.Longest Common Subsequence

  - dp，分两种情况，如果i位置和j位置元素一样，那看i-1 j-1即可
  - 如果i位置和j位置元素不一样，看i-1 j和j-1 i

- 718.Maximum Length of Repeated Subarray, 最长重复子数组

  - 子数组：连续的
  - $dp[i][j]= dp[i-1][j-1] + 1$

- 300.最长递增子序列

  - dp定义为以i结尾的最长连续递增序列
  - $if (nums[i] > nums[j]), dp[i] = max(dp[i], dp[j] + 1);$

- 674.最长连续递增序列

  - dp定义为以i结尾的最长连续递增序列

- 字符串转整数 itos

  - 循环结束之后还要看看Carry是否是0

- 整数反转

  - 

    ```python
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10
    
            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        
        return rev
    ```

    

- 912.快排

  - while left < right: ...

- 206.反转链表

  - 迭代

  - 递归写法：每次递归操作当前节点，令next指向prev；记录并将下一个需要处理的节点(next)和其prev(本node)传下去。

```python
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)
```

- 64 最小路径和
  - 注意边界初始化
  - 扩展：记录路径
    - 解法：dp倒着从右下角推，取上或左的最小即可。
  - <img src="/Users/tianran/Library/Application Support/typora-user-images/image-20220313152606411.png" alt="image-20220313152606411" style="zoom:25%;" />

- 83：删除排序链表中的重复元素 

  - 双指针：一个定在当前，另外一个往前走，碰见重复就往下过；碰见独特的就让prenext等于它，连起来
    - 注意这种方法要在循环结束后，让pre.next指向None
  - 如果忽略空间最优，可以新建一个list，边遍历边尾插

- 82 删除排序链表中的重复元素 2

  ```python
    def deleteDuplicates(self, head: ListNode) -> ListNode:
          if not head:
              return head  
          
    			dummy = ListNode(0, head)
  
          cur = dummy
          while cur.next and cur.next.next:
              if cur.next.val == cur.next.next.val:
                  x = cur.next.val
                  while cur.next and cur.next.val == x:
                      cur.next = cur.next.next
              else:
                  cur = cur.next
  
          return dummy.next
  ```

  

- 二维前缀和

  - 加矩形、加矩形、减重合
  - https://leetcode-cn.com/problems/matrix-block-sum/

- 计数排序

  - https://www.cnblogs.com/xiaochuan94/p/11198610.html

- 排序变种

- 排序时间和空间复杂度，归并排序空间复杂度可以为O(1)，怎么实现？

  - 取余数 但我不会做

- 1元、2元纸币，组成n元有多少种组合方式？

  - --->n/2+1 （完全背包 Knapsack algorithm
  - 背包

- 数据流中位数

- 数据流topk 

  - 空间复杂度低：堆[排序]()， 时间复杂度低：快速[排序]

- 单词接龙

- 平衡二叉树

- 栈实现队列

  - 倒腾

- 3sum

  - sort之后双指针

- 105.给定一棵二叉树的先序和中序遍历，重构这棵树

  - 递归法：preorder[0]做root，在inorder里找root的index，分成左右两块。按长度在preorder里找到左右两子树对应的slices，递归。

- 106.中序和后序重构

  - 递归法：postorder[-1]做root，在inorder里找root的index，分成左右两块。按长度在post-order里找到左右两子树对应的slices，递归。

- 将一个数变成另一个数的最小操作步骤

  - https://www.nowcoder.com/discuss/730673?type=2&order=0&pos=264&page=1&source_id=discuss_tag_nctrack&channel=-1&ncTraceId=779e511c8395432fb5d9fb2ddaa3fd37.195.16467322600170295&gio_id=9D875F72CEB56B6038BECAF599A839A6-1646730832369

- 旋转排序数组中的搜索

  - https://leetcode-cn.com/problems/search-in-rotated-sorted-array/ 

- 最小编辑距离

  - 

  - ```python
    class Solution:
        def minDistance(self, word1: str, word2: str) -> int:
            dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
            for i in range(len(word1)+1):
                dp[i][0] = i
            for j in range(len(word2)+1):
                dp[0][j] = j
            for i in range(1, len(word1)+1):
                for j in range(1, len(word2)+1):
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            return dp[-1][-1]
    ```

- LC315 计算右边小于当前的个数（Hard）

- 循环[链表](https://www.nowcoder.com/jump/super-jump/word?word=链表)入环处

- 滑动窗口最大值

  - Heap

- 221.最大正方形

  - 从右下遍历、dp

- 正、反、中序、层序遍历[二叉树](https://www.nowcoder.com/jump/super-jump/word?word=二叉树)

- 链表奇偶有序输出

- [算法题](https://www.nowcoder.com/jump/super-jump/word?word=算法题)：二维矩阵中两个点之间的最短路径（要讨论思路，时间、空间复杂度；可惜没有跑通😂）

- k组翻转链表

  - Dummy node initialization

    ```python
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
                print(pre.val,cur.val)
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                    print(dummy.next)
                jump.next = pre
                jump = l
                l = r
                
            else:
                return dummy.next
    ```

  

  

- binary search结束的时候，如果没有找到target，left会指向第一个大于target的数的index

- \34. Find First and Last Position of Element in Sorted Array

  - ```python
    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
        mid = (left + right) / 2
        if x >= A[mid]: left = mid + 1
        else: right = mid - 1
        return right 
        # right是mid更新来的。更新条件是A[mid] > target.
        # so, right右边的数肯定比target大，所以right是最右的、小于或等于target的数
    ```

    

做题曲线图：

3.30 199

3.14 186

3.13 184

3.9 180

3.6 175

2.16 146

2.1 131



