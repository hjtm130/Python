# 出力の総和：1

import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp( a-c ) # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    
    y = exp_a / sum_exp_a
    return y