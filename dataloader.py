import torch
from torch.utils.data import Dataset, DataLoader

import numpy as np

import os
import random

from PIL import Image, ImageOps

#import any other libraries you need below this line
from torchvision.transforms import functional as TF

class Cell_data(Dataset):
    def __init__(self, data_dir, size, train='True', train_test_split=0.8, augment_data=True):
        ##########################inputs##################################
        # data_dir(string) - directory of the data#########################
        # size(int) - size of the images you want to use###################
        # train(boolean) - train data or test data#########################
        # train_test_split(float) - the portion of the data for training###
        # augment_data(boolean) - use data augmentation or not#############
        super(Cell_data, self).__init__()
        # todo
        # initialize the data class
        self.data_dir = data_dir
        self.img_dir = os.path.join(self.data_dir, "scans")
        self.lbl_dir = os.path.join(self.data_dir, "labels")
        self.imgs = os.listdir(self.img_dir)
        self.lbls = os.listdir(self.lbl_dir)
        self.img_path = []
        self.lbl_path = []

        for img in self.imgs:
            self.img_path.append(os.path.join(self.img_dir, img))

        for lbl in self.lbls:
            self.lbl_path.append(os.path.join(self.lbl_dir, lbl))

        self.size = size
        self.train = train
        self.split = train_test_split
        self.augment = augment_data
        

    def __getitem__(self, idx):
        # todo
        # load image and mask from index idx of your data
        image = self.img_path[idx]
        label = self.lbl_path[idx]
        img = Image.open(image)
        lbl = Image.open(label)

        # # data augmentation part
        if self.augment_data:
            augment_mode = np.random.randint(0, 4)
            if augment_mode == 0:
                # todo
                # flip image vertically
                img = TF.vflip(img)
                lbl = TF.vflip(lbl)

            elif augment_mode == 1:
                # todo
                # flip image horizontally
                img = TF.hflip(img)
                lbl = TF.hflip(lbl)

            elif augment_mode == 2:
                # todo
                # zoom image
                w,h = img.size
                img = TF.center_crop(img, (h,w))
                lbl = TF.center_crop(lbl, (h,w))

            else:
                # todo
                # rotate image
                angle = random.randint(-45,45)
                img = TF.rotate(img,angle)
                lbl = TF.rotate(lbl,angle)

        # todo
        return img,lbl

    def __len__(self):
        return len(self.imgs)

