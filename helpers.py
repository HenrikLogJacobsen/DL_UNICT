from tqdm import tqdm
import numpy as np
import wfdb
import torch

def load_raw_data(df, sampling_rate = 100, path = '../input/ptb-xl-dataset/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1/'):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path+f) for f in tqdm(df.filename_lr)]
    else:
        data = [wfdb.rdsamp(path+f) for f in tqdm(df.filename_hr)]
    data = np.array([signal for signal, _ in data])
    return data

def to_tensor(x):
    return torch.tensor(x if isinstance(x, np.ndarray) else x.values, dtype=torch.float32)