快手一面 Mar31 

准备：

1. listToTree，想用 Map 实现O(n)，没做出来，面试官引导后也没做出来
   后来说要不让我重写一下 O(n2)，思路太乱了没写对

<img src="/Users/tianran/Library/Application Support/typora-user-images/image-20220331144030913.png" alt="image-20220331144030913" style="zoom:50%;" />

1.[最长回文子串](https://www.nowcoder.com/jump/super-jump/word?word=最长回文子串)

中心扩散法，要讨论长度为奇数还是偶数

2.八个铁球，一个轻的，几次可以找到轻的那个

2次，第一次3 3 2分，3和3上称。

3.排列组合，英雄联盟5v5,选择的英雄不能重复。一共有60个英雄。我方选择到孙悟空的概率是多少。

12分之一。

4.lr和svm的异同点

相同：不考虑kernel，都是linear的有监督分类算法，决策面都是线性的。也都是判别式模型。

不同：本质就是loss不同，svm是hinge loss，lr是celoss。

svm是结构风险最小化，包含了正则化项。lr是经验风险最小化。

svm复杂，适合小数据集。lr比较简单，大数据上比较合适，而且可以在线训练。

svm常用kernel来解决非线性问题。

svm考虑边界附近的点，lr考虑所有。



- 自己实现一个FreqStack，和普通stack的最大区别就是pop的是出现频率最大的元素

3、[leetcode](https://www.nowcoder.com/jump/super-jump/word?word=leetcode) 120题 三角形最小路径和

4、堆[排序](https://www.nowcoder.com/jump/super-jump/word?word=排序)给出结果



- 介绍几种决策树剪枝方法

- L1和l2如何解决过拟合
  

SQL问题：
Join 和 left join区别
如何理解开窗函数
一个SQL问题的思路（列转行



1.项目问题，测试过程

2.代码：最长不重复子串

指针，记录这个char上一次出现的位置，更新maxLen

3.针对他设置测试案例

4.微信发红包

5.数据库:多表，每个课程及格人数，连接查询比较好

6.反问

7.前面需要更广泛的测试用例