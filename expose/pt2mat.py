import os
from scipy.io import savemat
import torch
import numpy as np


def main(pt_path, mat_path):
    files = os.listdir(pt_path)

    for file in files:
        p = os.path.join(pt_path, file)
        if os.path.isfile(p):
            temp = np.array(torch.load(p))
            filename = file[:-2] + 'mat'
            save_path = os.path.join(mat_path, filename)
            savemat(save_path, mdict={'data': temp})


if __name__ == '__main__':
    main(pt_path='../data/pt_ntu_bin/test', mat_path='../data/pt_ntu_bin/mat2')
