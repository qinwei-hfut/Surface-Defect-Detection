import torch
import os
import numpy as np
import PIL
from PIL import Image
import pdb

def pil_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')

def pil_L_loader(path):
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('L')

def pil_1_loader(path):
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('1')

path = './PCBData/group00041/00041/'
for root, _, fnames in sorted(os.walk(path)):
    for fname in sorted(fnames):
        img = pil_1_loader(path+fname)
        pdb.set_trace()
