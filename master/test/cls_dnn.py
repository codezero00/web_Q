"""

"""
import re
import jieba
import numpy as np
import torch
from torch import nn, optim
from torch.autograd import Variable


lx_map = {
3:"轨道交通管理",
10:"铁路方面的问题",
13:"积水问题",
15:"水污染问题",
16:"异味污染问题",
18:"电磁辐射污染问题",
19:"房屋安全",
20:"房产收费问题",
22:"工地周边问题",
23:"合同纠纷",
25:"医学美容纠纷",
30:"医院管理问题",
31:"医药收费问题",
32:"学生补课问题",
33:"教育培训机构",
34:"幼儿教育问题",
38:"社区建设",
46:"交通事故处理",
47:"交通违法处理",
54:"小区绿化问题",
59:"工业噪声问题",
60:"生活噪声问题",
61:"商业噪音问题",
63:"私搭乱建",
64:"占道经营",
65:"油烟污染",
66:"工地噪音",
67:"建筑垃圾",
68:"路面破损",
69:"道路不洁",
70:"生活垃圾",
73:"违规占用、挖掘道路",
74:"焚烧垃圾",
75:"擅自饲养家禽家畜",
79:"下水道堵塞或破损",
80:"其它市容环境管理问题",
83:"物业纠纷",
84:"商品房买卖纠纷",
86:"房屋产权问题",
88:"房屋建设规划问题",
90:"房屋质量问题",
91:"其它房屋土地管理问题",
}



r = '[’!，。\n\s"#$%&\'()（）【】“”*+,-./:;<=>?@[\\]^_`{|}~]+'

def fc(line):
    """
    分词函数+去标点符号
    :param line:
    :return:
    """
    line = line.strip()
    line = re.sub(r, '', line)
    seg_list = jieba.cut(line, cut_all=False)  # 返回生成器
    return seg_list

###############################数据预处理#######################################



def forecast(content):
    content_list = list(fc(content))
    import pickle
    with open('word2idx.pkl', 'rb') as f:
        word2idx = pickle.load(f)
    # idx2word = {word2idx[word]: word for word in word2idx}
    # wordnum2 = list(map(lambda x: word2idx[x], content_list))+[0]*(400-len(content_list))  # word2idx[x] 导致keyerror bug
    ## 利用dict内置的get(key[,default])方法，如果key存在，则返回其value,否则返回default;使用这个方法永远不会触发KeyError
    wordnum2 = list(map(lambda x: word2idx.get(x, 0), content_list)) + [0] * (400 - len(content_list))


    # list 转换为矩阵
    np_wordnum2 = np.array(wordnum2)

    # narray转换为tensor
    trainX = torch.LongTensor(np_wordnum2)
    trainX = trainX.view(1, 400)  # 转换矩阵格式


    model = torch.load('cnntext_91_2.pkl')
    # print(model)

    model.eval()
    b_x = Variable(trainX)
    out = model(b_x)
    _, pred = torch.max(out, 1)  # pred 为预测结果

    # print(_)
    # print(int(pred.data))
    lx_int = int(pred.data)
    return lx_map[lx_int]


