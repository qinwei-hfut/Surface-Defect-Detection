import torch
import os
import numpy as np
import PIL
from PIL import Image
import pdb
import random
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

def add_lines(np_img):
    np_img = np_img.copy()
    line_num = random.randint(5,20)
    for i in range(line_num):
        length = random.randint(120,450)
        width = random.randint(1,3)
        left_up_pos_x = random.randint(0,500)
        left_up_pos_y = random.randint(0,200)
        for x_p in range(left_up_pos_x,left_up_pos_x+width):
            for y_p in range(left_up_pos_y,left_up_pos_y+length):
                if x_p < 640 and y_p < 640:
                    # np_img[x_p][y_p] = np.abs(np_img[x_p][y_p] - 255)
                    np_img[x_p][y_p] = 255
    return np_img

def iverse_point(np_img):
    np_img = np_img.copy()
    for xp in range(0,635):
        for yp in range(0,635):
            if (np_img[xp][yp] != np_img[xp+2][yp]).any():
                if random.randint(1,10) < 4:
                    np_img[xp][yp] = np.abs(np_img[xp][yp] - 255)
            if (np_img[xp][yp] != np_img[xp][yp+2]).any():
                if random.randint(1,10) < 4:
                    np_img[xp][yp] = np.abs(np_img[xp][yp] - 255)
    return np_img



path = './PCBData/group00041/00041/'
save_path = './PCBData/group00041/00041_g/'
if not os.path.exists(save_path):
    os.makedirs(save_path)
for root, _, fnames in sorted(os.walk(path)):
    for fname in sorted(fnames):
        if 'test' in fname:
            continue
        img = pil_loader(path+fname)
        np_img = np.asarray(img)
        # pil_img = Image.fromarray(np_img,mode='1')
        np_img = iverse_point(np_img)
        np_img = add_lines(np_img)
        pil_img = Image.fromarray(np_img)
        pil_img.save(save_path+fname)
        # pdb.set_trace()
