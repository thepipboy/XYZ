import numpy as np

def NNNtensor():
    NNNtensor1 = np.array([[1, 0, 0, 0, 1],
                           [1, 1, 0, 0, 1],
                           [1, 0, 1, 0, 1],
                           [1, 0, 0, 1, 1],
                           [1, 0, 0, 0, 1]])

    NNNtensor2 = np.array([[2, 0, 0, 0, 2],
                           [2, 2, 0, 0, 2],
                           [2, 0, 2, 0, 2],
                           [2, 0, 0, 0, 2],
                           [2, 0, 0, 2, 0]])

    NNNtensor3 = np.array([[3, 0, 0, 0, 3],
                           [3, 3, 0, 0, 3],
                           [3, 0, 3, 0, 3],
                           [3, 0, 0, 3, 3],
                           [3, 0, 0, 0, 3]])

    NNNtensor4 = np.array([[4, 0, 0, 0, 4],
                           [4, 4, 0, 0, 4],
                           [4, 0, 4, 0, 4],
                           [4, 0, 0, 4, 4],
                           [4, 0, 0, 0, 4]])

    NNNtensor5 = np.array([[5, 0, 0, 0, 5],
                           [5, 5, 0, 0, 5],
                           [5, 0, 5, 0, 5],
                           [5, 0, 0, 0, 5],
                           [5, 0, 0, 0, 0]])

    NNNtensor6 = np.array([[6, 0, 0, 0, 6],
                           [6, 6, 0, 0, 6],
                           [6, 0, 0, 0, 6],
                           [6, 0, 0, 0, 6],
                           [6, 0, 0, 0, 6]])

    NNNtensor7 = np.array([[7, 0, 0, 0, 7],
                           [7, 7, 0, 0, 7],
                           [7, 0, 7, 0, 7],
                           [7, 0, 0, 7, 7],
                           [7, 0, 0, 0, 7]])

    NNNtensor8= np.array([[8, 0, 0, 0, 8],
                          [8, 8, 0, 0, 8],
                          [8, 0, 8, 0, 8],
                          [8, 0, 0, 0, 8],
                          [8, 0, 0, 0, 8]])

    NNNtensor9 = np.array([[9, 0, 0, 0, 9],
                           [9, 9, 0, 0, 9],
                           [9, 0, 9, 0, 9],
                           [9, 0, 0, 0, 9],
                           [9, 0, 0, 0, 9]])

    return [NNNtensor1, NNNtensor2, NNNtensor3, NNNtensor4, NNNtensor5, NNNtensor6, NNNtensor7, NNNtensor8, NNNtensor9]
print(NNNtensor)