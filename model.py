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
    self.layer_1 = twoConvBlock(1,64)
    self.pool_1 = nn.MaxPool2D(2,stride=2)
    self.layer_2 = twoConvBlock(64,128)
    self.layer_3 = twoConvBlock(128,256)
    self.layer_4 = twoConvBlock(256,512)
    self.layer_5 = twoConvBlock(512,1024)

  def forward(self,input):
    #todo
    #implement the forward path
    conv_layer_1 = self.layer_1(input)
    pool = self.pool_1(conv_layer_1)

    conv_layer_2 = self.layer_2(pool)
    pool = self.pool_1(conv_layer_2)

    conv_layer_3 = self.layer_3(pool)
    pool = self.pool_1(conv_layer_3)

    conv_layer_4 = self.layer_4(pool)
    pool = self.pool_1(conv_layer_4)

    output = self.layer_5(pool)

    return output, conv_layer_1, conv_layer_2, conv_layer_3, conv_layer_4

class upStep(nn.Module):
  def __init__(self):
    super(upStep, self).__init__()
    #todo
    #initialize the up path
    self.upsample = nn.Upsample(scale_factor = 2, align_corners = True)
    self.layer_1 = twoConvBlock(1024,512)
    self.layer_2 = twoConvBlock(512,256)
    self.layer_3 = twoConvBlock(256, 128)
    self.layer_4 = twoConvBlock(128,64)
    self.layer_5 = nn.Conv2D(64,2,1)

  def forward(self, input,skip_1,skip_2,skip_3,skip_4):
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







