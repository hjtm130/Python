import numpy as np

# ベクトルの作成
# Numpyで1次元配列を作成する
# 行ベクトルを作成
vector_row = np.array([1,2,3])
# 列ベクトルを作成
vector_column = np.array([[1],
                          [2],
                          [3]])

# 行列の作成
# Numpyで2次元配列を作成
# 行列の作成
matrix = np.array([[1,2],
                   [1,2],
                   [1,2]])

# 非0要素が少ししかないデータを効率的に表現する
# 疎行列の作成
from scipy import sparse
# 行列の作成
matrix = np.array([[0,0],
                   [0,1],
                   [3,0]])
# CSR(compressed sparse row)形式の行列を作る
matrix_sparse = sparse.csr_matrix(matrix)
# 疎行列を表示
print(matrix_sparse)

# ベクトルや行列から要素を選択する
vector = np.array([1,2,3,4,5,6])
# 行列を作成
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])