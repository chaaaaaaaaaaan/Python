# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:19:41 2021

@author: mteg_label3
"""

import pandas as pd
import matplotlib.pyplot as plt
import xmltodict, json
import seaborn as sns

fdir=r'C:\Users\mteg_label3\Desktop\python\과제3\\'
fn='aaaa0012_2020042505_train_2020_10_21_detect_2020_11_09.txt'

with open(fdir+fn,'rt',encoding='UTF8') as fd:
    detect=pd.read_csv(fd,delimiter='\t',names=['Frame','class No','class name', 
                                    'bbox1','bbox2','bbox3','bbox4','accuracy'])
   
fr=30

fdir1=r"C:\Users\mteg_label3\Downloads\MtegLabelTool_v0.6.1\\"
fn1="labels.xml"
with open(fdir1+fn1) as fd:
    label = xmltodict.parse(fd.read())
label=json.loads(json.dumps(label))
label=pd.DataFrame(label['ArrayOfLabelObject']['LabelObject'],columns=["name","clr"])


#ti=str(datetime.timedelta(seconds=int(detect['Frame'][len(detect)-1])/fr))
detect.plot.scatter(x='Frame', y='class name',marker='|',color='c')

#sns.scatterplot(x='Frame', y='class name', marker='|', 
#                data=detect,hue='class name')
plt.show()

