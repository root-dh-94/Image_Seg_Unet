import torch
import torch.nn as nn
import torch.nn.functional as F

#import any other libraries you need below this line

class twoConvBlock(nn.Module):
  def __init__(self, in_ch,out_ch):
    super(twoConvBlock, self).__init__()
    #todo
    #initialize the block
    self.input_channel = in_ch
    self.output_channel = out_ch
    self.layer_block = nn.Sequntial(nn.Conv2D(self.input_channel,self.output_channel,3),nn.ReLU(),nn.Conv2D(self.output_channel,oself.output_channel,3),nn.BatchNorm2d(self.output_channel),nn.ReLU())

  def forward(self,input):
    #todo
    #implement the forward path
    block = self.layer_block(input)
    return block

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
    self.upsample = nn.Upsample(scale_factor = 2, mode = "bilinear" align_corners = True)
    self.layer_1 = twoConvBlock(1024,512)
    self.layer_2 = twoConvBlock(512,256)
    self.layer_3 = twoConvBlock(256, 128)
    self.layer_4 = twoConvBlock(128,64)
    self.layer_5 = nn.Conv2D(64,2,1)

  def forward(self, input,skip_1,skip_2,skip_3,skip_4):
    #todo
    #implement the forward path
    upsample = self.upsample(input)
    up_layer_1 = self.layer_1(torch.cat((skip_4,upsample)))

    upsample = self.upsample(up_layer_1)
    up_layer_2 = self.layer_2(torch.cat((skip_3,upsample)))

    upsample = self.upsample(up_layer_2)
    up_layer_3 = self.layer_3(torch.cat((skip_2,upsample)))

    upsample = self.upsample(up_layer_3)
    up_layer_4 = self.layer_4(torch.cat((skip_1,upsample)))

    output = self.layer_5(up_layer_4)

    return output

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
    down,skip_1,skip_2,skip_3,skip_4 = self.downStep(input)
    output = self.upStep(down,skip_1,skip_2,skip_3,skip_4)

    return output
    
    







