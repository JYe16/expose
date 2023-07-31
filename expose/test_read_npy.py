import numpy as np
import torch

if __name__ == '__main__':
    npz = np.load('/mnt/h/Datasets/Own/img/0606-yzk-play-phone1/test/0000.jpg_000_params.npz')
    tt = torch.load('/mnt/d/yzk/NTU/base_joint_pt_single/train/S001C001P001R001A002_base_joint.pt')
    print(tt)