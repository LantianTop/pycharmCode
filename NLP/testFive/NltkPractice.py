#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年05月11日15时59分45秒
import nltk
import nltk.book as nb
# # 第一章课后习题第五题
# # print("根据对比，在表中言情小说的词汇多样性得分更高，所以词汇更丰富！")
# # # 第一章课后习题第六题
nb.text2.dispersion_plot(['Elinor','Edward','Willoughby','Marianne'])
 # 第一章课后习题第21题
 # nb.text2[-2:]
# 第一章课后习题第22题
text5_fq=nltk.FreqDist(w for w in nb.text5 if len(w)==4)
print(sorted(text5_fq,key=lambda x:text5_fq[x],reverse=True))