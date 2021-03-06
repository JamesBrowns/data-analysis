#coding=utf-8
import pandas as pd
from scipy.interpolate import lagrange
'''
inputfile='test/data/missing_data.xls'
outputfile='test/tmp/1112.xls'
data=pd.read_excel(inputfile,header=None)


def ployinterp_column(s,n,k=5):
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    y=y[y.notnull()]
    return lagrange(y.index,list(y))(n)
for i in data.columns:
    for j in range(len(data)):
        
        if (data[i].isnull())[j]:
            data[i][j]=ployinterp_column(data[i],j)

data.to_excel(outputfile,header=None,index=False)

'''
'''
import random
inputfile='test/data/model.xls'
data=pd.read_excel(inputfile)
data=data.as_matrix()
random.shuffle(data)

p=0.8
train=data[:int(len(data)*p),:]
test=data[int(len(data)*p):,:]

from keras.models import Sequential
from keras.layers.core import Dense,Activation
outnetfile='test/tmp/net.model'

net=Sequential()
net.add(Dense(3,10))
net.add(Activation('relu'))
net.add(Dense(10,1))
net.add(Activation('sigmoid'))
net.compile(lose='binary_crossentropy',optimizer='adam',class_mode='binary')

net.fit(train[:,:3],train[:,3],nb_epoch=1000,batch_sizer=1)
net.save_weight(outnetfile)

predict_result=net.predict_class(train[:,:3]).reshap(len(train))

from cm_plot import *
cm_plot(train[:,3],predict_result).show

'''
#-*- coding: utf-8 -*-

import pandas as pd
from random import shuffle

datafile = 'test/data/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

from keras.models import Sequential #导入神经网络初始化函数
from keras.layers.core import Dense, Activation #导入神经网络层函数、激活函数

netfile = 'test/tmp/net.model' #构建的神经网络模型存储路径

net = Sequential() #建立神经网络
net.add(Dense(3, 10)) #添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation('relu')) #隐藏层使用relu激活函数
net.add(Dense(10, 1)) #添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid')) #输出层使用sigmoid激活函数
net.compile(loss = 'binary_crossentropy', optimizer = 'adam', class_mode = "binary") #编译模型，使用adam方法求解

net.fit(train[:,:3], train[:,3], nb_epoch=1000, batch_size=1) #训练模型，循环1000次
net.save_weights(netfile) #保存模型

from sklearn.metrics import confusion_matrix #导入混淆矩阵函数

predict_result = net.predict_classes(train[:,:3]).reshape(len(train)) #预测结果变形
'''这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n'''

cm = confusion_matrix(train[:,3], predict_result) #混淆矩阵

import matplotlib.pyplot as plt #导入作图库
plt.matshow(cm, cmap=plt.cm.Greens) #画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
plt.colorbar() #颜色标签

for x in range(len(cm)): #数据标签
  for y in range(len(cm)):
    plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

plt.ylabel('True label') #坐标轴标签
plt.xlabel('Predicted label') #坐标轴标签
plt.show() #显示作图结果

        
