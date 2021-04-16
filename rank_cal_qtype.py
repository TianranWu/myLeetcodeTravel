#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pickle


def rank(scores1, scores2, idx_q, labels):

    # Accuracy variables
    med_rank1 = []
    recall1 = {1: 0.0, 5: 0.0, 10: 0.0, 100: 0.0}

    med_rank2 = []
    recall2 = {1: 0.0, 5: 0.0, 10: 0.0, 100: 0.0}

    unique_idxs = np.unique(idx_q)
    N = len(unique_idxs)

    for iq in unique_idxs:

        pos_iq = np.where(idx_q  == iq)
        this_labels = labels[pos_iq]
        ir = np.where(this_labels == 1)[0]
        this_scores1 = scores1[pos_iq]
        this_scores2 = scores2[pos_iq]

        ranking1 = np.argsort(this_scores1).tolist()
        ranking2 = np.argsort(this_scores2)[::-1].tolist()

        # position of idx in ranking
        pos1 = ranking1.index(ir)
        if (pos1 + 1) == 1:
            recall1[1] += 1
        if (pos1 + 1) <= 5:
            recall1[5] += 1
        if (pos1 + 1) <= 10:
            recall1[10] += 1
        if (pos1 + 1) <= 100:
            recall1[100] += 1

        # store the position
        med_rank1.append(pos1 + 1)

        pos2 = ranking2.index(ir)
        if (pos2 + 1) == 1:
            recall2[1] += 1
        if (pos2 + 1) <= 5:
            recall2[5] += 1
        if (pos2 + 1) <= 10:
            recall2[10] += 1
        if (pos2 + 1) <= 100:
            recall2[100] += 1

        # store the position
        med_rank2.append(pos1 + 1)

    for i in recall1.keys():
        recall1[i] = recall1[i] / N

    for i in recall2.keys():
        recall2[i] = recall2[i] / N

    return np.median(med_rank1), recall1, np.median(med_rank2), recall2


# In[2]:


def load_obj(filename):
    f = open(filename, 'rb')
    obj = pickle.load(f)
    f.close()
    print("Load object from %s." % filename)
    return obj


def rank_by_qtype(q_type, type_idx_dict, l,s,ii):
    
    # The Index of this question type
    q_idx = type_idx_dict[q_type]
    
    end_num = ii[-1]
    kb_len = int(len(l)/(end_num+1))
    
    # Initialization
    new_label = []
    new_scores = []
    new_idx = []
    
    
    for i in range(int(end_num)+1):
    #     print(f_i[i*kb_len:(i+1)*kb_len])
        if i in q_idx:
            new_label.append(l[i*kb_len:(i+1)*kb_len])
            new_scores.append(s[i*kb_len:(i+1)*kb_len])
            new_idx.append(ii[i*kb_len:(i+1)*kb_len])
#         print(new_label)
    
    
    
    new_label = np.array(new_label).reshape(-1,1)
    new_scores = np.array(new_scores).reshape(-1,1)
    new_idx = np.array(new_idx).reshape(-1,1)
    
    print(new_label.shape)
    
    Med, recall1, _, _, = rank(new_scores,new_scores,new_idx,new_label)
    return Med, recall1


# In[3]:


f_label = '/Users/tianran/Documents/GitHub/friends-new/Data/0407_FT_both_retrieval_labels_test.pckl'
f_idx = '/Users/tianran/Documents/GitHub/friends-new/Data/0407_FT_both_retrieval_idxq_test.pckl'
f_score = '/Users/tianran/Documents/GitHub/friends-new/Data/0407_FT_both_retieval_scores_test.pckl'

f_l = load_obj(f_label)
f_s = load_obj(f_score)
f_i = load_obj(f_idx)
print(type(f_l),f_l.size)
print(f_l.shape)
end_num = f_i[-1]
print(end_num)
kb_len = int(len(f_l)/(end_num+1))
print('kb len for friends:', kb_len)


# In[6]:


qtype_idx_dict = load_obj('obj/friends_qtype_to_idx.pkl')


# In[8]:


for qname in qtype_idx_dict.keys():
    print(qname)


# In[9]:



for qname in qtype_idx_dict.keys():
    print(qname, rank_by_qtype(qname,qtype_idx_dict,f_l,f_s,f_i))


# In[10]:


# T_label = '/Users/tianran/Documents/GitHub/friends-new/Data/TBBT_retrieval/0407_Simple_Trans_both_retrieval_labels_testboth_retrfromTBBT.pckl'
# T_idx = '/Users/tianran/Documents/GitHub/friends-new/Data/TBBT_retrieval/0407_Simple_Trans_both_retrieval_idxq_testbothretrfromTBBT.pckl'
# T_score = '/Users/tianran/Documents/GitHub/friends-new/Data/TBBT_retrieval/0407_Simple_Trans_both_retrieval_scores_testbothretrfromTBBT.pckl'

T_label = '/Users/tianran/Documents/GitHub/friends-new/Data/TBBT_retrieval/FT_both1_retrieval_labels_test.pckl'
T_idx = '/Users/tianran/Documents/GitHub/friends-new/Data/TBBT_retrieval/FT_both1_retrieval_idxq_test.pckl'
T_score = '/Users/tianran/Documents/GitHub/friends-new/Data/TBBT_retrieval/FT_both1_retrieval_scores_test.pckl'


T_l = load_obj(T_label)
T_s = load_obj(T_score)
T_i = load_obj(T_idx)
print(type(T_l),T_l.size)
print(len(T_l),len(T_s),len(T_i))
print(T_l.shape)
end_num = T_i[-1]
print('End_num for TBBT:', end_num)
kb_len = int(len(T_l)/(end_num+1))
print('KB len for TBBT:', kb_len)


# In[13]:


knowit_qtype_idx_dict = load_obj('obj/knowit_qtype_to_idx.pkl')


# In[14]:


rank_by_qtype('who',knowit_qtype_idx_dict,T_l,T_s,T_i)


# In[15]:


for qname in knowit_qtype_idx_dict.keys():
    print(qname, rank_by_qtype(qname,knowit_qtype_idx_dict,T_l,T_s,T_i))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




