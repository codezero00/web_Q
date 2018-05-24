import numpy as np
import gensim

model = gensim.models.word2vec.Word2Vec.load('word2vec_wx')


def predict_proba(oword, iword):
    '''
    参考gensim中的Word2Vec的score_sg_pair函数写的，简单的流程是：取出wk的Huffman编码（路径），取出wi的词向量，然后根据路径，要把路径上每个节点的概率都算出来，然后乘起来，得到p(wk|wi)。这是算得是概率对数，应该乘法变为加法。最后的概率是怎么计算的呢？事实上，按照Word2Vec的公式，每个节点的概率对数是：
    ==log(11+e−x⊤θ)1−d(1−11+e−x⊤θ)d−(1−d)log(1+e−x⊤θ)−dlog(1+e−x⊤θ)−dx⊤θ−log(1+e−x⊤θ)−dx⊤θ

    这里的θ是节点向量，x是输入词向量，d是该节点的编码（非0即1）。但是，官方的score_sg_pair函数并不是这样写的，那是因为
    ===−log(1+e−x⊤θ)−dx⊤θ−log[edx⊤θ(1+e−x⊤θ)]−log(edx⊤θ+e(d−1)x⊤θ)−log(1+e−(−1)dx⊤θ)
    :param oword:
    :param iword:
    :return:
    '''
    iword_vec = model[iword]
    oword = model.wv.vocab[oword]
    oword_l = model.syn1[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code * dot)
    return lprob


from collections import Counter


def keywords(s):
    s = [w for w in s if w in model]
    ws = {w: sum([predict_proba(u, w) for u in s]) for w in s}
    return Counter(ws).most_common()


import pandas as pd  # 引入它主要是为了更好的显示效果
import jieba




def GenKeywords(content):
    x = jieba.cut(content)
    return list(map(lambda x: x[0], keywords(x)))[0:5]


if __name__ == '__main__':
    s = u'''

    我是移动的手机用户，2013年的时候，我在移动营业厅办理了一个月租88元钱的套餐，
    后来2015年的时候，我想要更换资费，但工作人员称我有2年合约，
    要等到2年期满之后才能改，后来我忘了此事，直到今年8月份的时候，
    我又向移动客服反映了此事，工作人员却称我的号码是靓号，
    永久不能更改套餐，但是我并不知情，其也提供不出来证据证明此事，
    至今移动都未给我一个合理答复，我觉得很不合理，我要求移动公司更改我的资费，
    并且对于这两年我因此事造成的损失，给予赔偿

    '''
    # x = pd.Series(keywords(jieba.cut(s)))
    # x = list(map(lambda x:x[0],keywords(jieba.cut(s))))[0:5]
    # print(x)
    x = GenKeywords(s)
    print(x)