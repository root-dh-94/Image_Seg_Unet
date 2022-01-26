import torch
import torch.nn as nn
import torch.nn.functional as F

#import any other libraries you need below this line

class twoConvBlock(nn.Module):
  def __init__(self, in_ch,out_ch):
    super(twoConvBlock, self).__init__()
    #todo
    #initialize the block
    self.layer_block = nn.Sequntial(nn.Conv2D(in_ch,out_ch,3),nn.ReLU(),nn.Conv2D(out_ch,out_ch,3),nn.BatchNorm2d(out_ch),nn.ReLU())

  def forward(self,input):
    #todo
    #implement the forward path
    block = self.layer_block(input)
    return input

class downStep(nn.Module):
  def __init__(self):
    super(downStep, self).__init__()
    #todo
    #initialize the down path

  def forward(self):
    #todo
    #implement the forward path

class upStep(nn.Module):
  def __init__(self):
    super(upStep, self).__init__()
    #todo
    #initialize the up path

  def forward(self):
    #todo
    #implement the forward path

class UNet(nn.Module):
  def __init__(self):
    super(UNet, self).__init__()
    #todo
    #initialize the complete model
    self.downStep = downStep()
    self.upStep = upStep()

  def forward(self, input):
    #todo
    #implement the forward path
    layer_1 = self.downStep
    pool_1 = nn.MaxPool2d(2, stride = 2)(layer_1)
    layer_2 = self.downStep
    pool_2 = nn.MaxPool2d(2, stride = 2)(layer_1)
    layer_3 = self.downStep
    pool_3 = nn.MaxPool2d(2, stride = 2)(layer_1)
    layer_4 = self.downStep
    pool_4 = nn.MaxPool2d(2, stride = 2)(layer_1)
    layer_5 = self.downStep







