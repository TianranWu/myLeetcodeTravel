## Interview 

[toc]

## Introduction

Hello, I am Tianran Wu from Hulu, I graduated from Osaka University last October. 

I am fluent in English and got a 161/180 in JLPT N2. 

My research interests include deep learning, computer vision, and multi-modal learning. I have two papers that got accepted by BMVC 2021 and this year's ICIP. One is during my master's study. The other is done during my 4-month internship at Xiaomi Tokyo. As for software language, I am familiar with Python and Pytorch. I also know how to use Matlab and C. 


## Projects

### Hulu: GNN-based malicious account detection method

**Situation:** 

- 攻击、共享、薅羊毛

- 线上模型比较分散，有的无监督有的有监督，分数无法fusion，难以对一用户构造一个统一的危险系数分

- 时间聚集性和设备聚集性

- LSTM和GNN

**Task:**

- daily run，评分。高可疑，高评分。

- General评分框架，把线上的独立模型打通，每一个用户都有一个可以同级比较的分。

**Action:**

- 时序特征，1hr的session count

- metadata特征

- cross特征

- 统计特征

- 正样本：线上模型的结果，负样本：randomly selected

- 模型上：GraphSage，异构图，Attention结构，LSTM based Embeddings

**Result:**

- Recall 95%，

- Precision 97%

### Xiaomi Japan: High Dynamic Range Imaging with Multi-exposure Binning on Quad Bayer Color Filter Array

Situation:

- Quad Bayer: popular widely used sensor in Smart Phones, 因为高分辨率在相对比较小的手机屏幕上比较冗余，所以用QB结构实现two modes which is high resolution mode and lower resolution mode。其实就是牺牲一部分resolution换取Sensor的快速读取和响应，同时应对一些过饱和问题。

（Quad Bayer是一种sensor结构，相对于之前的RGGB阵列来说，QuadBayer以4个同颜色像素为一组。主要是为了实现拍照时的模式切换，高清模式和节能模式。这主要是因为现在的拍照像素相对于手机屏幕大小来说稍微有点冗余了。IPhone14 Pro，小米12Pro，三星 Galaxy A70都在用这个结构。）

Task:

HDR

Action:

我们引入了Multi exposure level binning的方法在sensor上进行读取。

（Multi exposure是什么，它能在硬件上简单实现）

读取时间相对于完全读取缩短四分之三。其二是我们的HDR imaging 阶段， 使用了一个对称结构的Unet来实现。

（4个Enc Blocks， 4个Dec Blocks，每个包含2层Conv层。Loss是一个MSE loss，但loss并非是在raw图做的，而是在tone mapping后的domain算的。）

Results:

实验结果上，用的是Funt 和Kalantari这两个公开的HDR数据集上的测试结果，指标包括PSNR，SSIM和HDR-VDP-2这些质量指标。同时我们也在意参数和计算量。

和SOTA比，计算量上是STOA的70分之一，参数量是60%，质量完全超越；和完全读取比，计算量是四分之一，质量持平，证明Unet足够有能力复原在读取阶段失去的四分之三像素内容。

这篇工作现在在ICIP审核中。


### Transfer Learning in Knowledge-based Video Question Answering (VideoQA)

**Situation:** VideoQA, challenging work. Few existing datasets. Knowledge base. Separated thing. can be reused without retraining.

**Task:** Study how the knowledge learned by the model is generalized for different domains.

**Action:**

- New dataset, clean it

- split the knowledge into two types. 

- propose two modules to mitigate the gap between the knowledge in the source and target dataset.
- DET
- Data augmentation

**Result:**

- boost the performance



### UVQA project

**Situation:** VideoQA, challenging work. Few existing datasets. 

Task: we want to generate image-relevant QA pairs, and use them as training samples to boost the performance.

**Action:**

- DAE, to train an encoder-decoder that can denoise sentences
- Ae-Adv loss to generate question-like sentences, using the decoder from the DAE
- Policy gradient method to generate relevant sentences

**Result:**

ongoing work.



### Dynamic stride DNN design

To achieve a reduction in computation while preserving accuracy, we need to correctly figure out the unimportant layers in the network. And tune their strides.  

We use gate modules to judge the importance. And, We formulate the dynamic tunning problem in the context of sequential decision making. This discrete decision is not differentiable. So we propose to combine supervised learning and reinforcement learning (policy gradient) to address it. 



**Gate module**

We achieve the dynamic tuning of stride by putting gate module over residual blocks.

Gate contains max-pooling, Conv layers, Avg-pooling and FC layers. (Or Maxpooling, Conv, RNN and FC)

After an  average  pooling  on  the  input  features,  we  apply  a $1×1$ convolution layer to reshape the features to a size $S$. Then, aLong Short Term Memory (LSTM) layer with hidden size of $S$ is  adopted. We employ a linear layer, mapping the output of LSTM layer to an $m×1$ vector to get the final stride choice. $m$ stands for the number of stride candidates and $S$​​ represents the embedding size of LSTM.

**Training**

**Gate made the decision:**

$Π(x_i,i) = P(G_i(x_i) = g_i)$​​​, where $g_i \in {1,2,3}$​​

We define the reward of each gating module as $R_i = g_i$ to encouragea large value as the output of a certain gate module.

The **reward** for a complete dynamic network is:

$r = \frac \alpha N \sum_{i=1}^N R_i$​​

So the **loss function**:

$L_{HR} = L(\tilde y, y) - \frac \alpha N \sum_{i=1}^N R_i$​​



![image-20220331164319399](/Users/tianran/Library/Application Support/typora-user-images/image-20220331164319399.png)



The **algorithm:**

![image-20211104123352855](/Users/tianran/Library/Application Support/typora-user-images/image-20211104123352855.png)

Result:

We also do a 8-bit quantizatioin after the dynamic structure to test the robustness. As a result, we **saved up to 50% computation amount** and **75% storage for ResNet-50**, without sacrifice on accuracy.



## My intern @Huawei

**Situation:** I work with Huawei Central Hardware Research center team to study how can we accelerate the training/evaluation of DNNs. Because Huawei, as a large company they usually deal with extremely large-scale datasets, the train of which is rather costing. Also, that hinders the wider use on edge devices.

A natural way to "compress the network".

3 ways to compress neural networks. - quantization.

At that time, quantization of a neural networks usually use a fixed bitwidth across all layers. However, the saliency/importance of different layers, are different. Some layers are vulnerable(like the first and the last layers). Some are robust. **(Task)** **So we research on heterogeneous bit-width quantization.** 

**Action:** How to weight the saliency? This touches the explainable machine learning, so we use variational bayesian based method. Instead of a single value parameter, we assign every parameter a mean and a variance. they are trained together. And we can get the SNR through them-that is the saliency.

**Result:** In the end we achieve 16x decrease for Resnet storage.



## Programming





### Other

I want to join as an intern if it is possible. I can work remotely until next March, as I am still a RA in our lab. I will be able to work on-site after April. 

Questions:

- How to train our entry level new employees? Will us be assigned with a mentor after entering into the company?
- More application or research job? or developper job?
- Is there any chances that I can be relocate back to China after 3 years.

HR



## Incubit Inc preparation

- **Interview with our HR**: You will be asked some basic questions about your background, motivation, and personality. You can also ask questions about us - so that we can make sure your and our expectations are in alignment.

  - BG: Tianran Wu from Osaka university currentky I am a english course master student in the second year. And will be graduate this septerember. My major is computer science.

    - My research is mostly about computer vision. My work is mainly to promote the deeper understanding of image and videos. 

    - Also, I am experienced with multi modal learning, this is, the co-operation of both language and vision. I tell the machine how to deeply understand, for exmaple, a TV drama, by asking them to answer my question. 
    - Further, I have experienced with model compression. This is to make a big/slow model to run in a real-time manner, or make it small, friendly for real-world or daily use.

  - Motivation:

    - I know Incubit in Linkedin. The first thing I notice is that, your information/requirements for candidates are very different from others. You do not only list what you want, but introduce your company in a very detailed and interesting way. 
    - I like the ways you interview the candidates, like do a kaggle challend, like in the final round all the members will have a joint meeting. 
    - Also your webpage is very attractive, through reading it I found that I just love what you are doing: to help the companies, to solve concrete daily problems, to let more people benefit from the AI technology.
    - And I myself, I think, I have the qulifications you need: I am familiar with coding, experienced with machine learning related research. I think these fit the requirements. So that is why I apply for this position. 

  - My personality

    - I am a quite out-going person. Currently I am in a Lab with multi-culture background. My supervisors and collegues coming from Canada, Spain, Japan, Vietnum and India. We get algong very well.
    - I have a cute cat in my place, and I like cooking. I am always the person who invite people home to eat together.
    - Overall, I think I am hard-working. 

- Other

  Questions:

  -  What is your most valued expectations for the candates at this positioin?
  - I apply both positions, so what will the Interview process be? 
    - I want to join as an intern if it is possible. I can work remotely until next March, as I am still a RA in our lab. I will be able to work on-site after April. 

  

  

## 谷歌karat

- 需要复习：

  - 怎么写链表、树的定义






- - 
