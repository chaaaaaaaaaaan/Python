# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:08:41 2021

@author: mteg_label3
"""

import pandas as pd
import xml.etree.ElementTree as ET
import xmltodict, json

#xml file
fdir= r"C:\Users\mteg_label3\Desktop\python\\"
fn="aaaa0008_201909020002"

#labels file
fdir1=r"C:\Users\mteg_label3\Downloads\MtegLabelTool_v0.6.1\\"
fn1="labels.xml"

#bbox xml file
#fdir2=r"C:\Users\mteg_label3\Desktop\python\aaaa0008_201909020002\\"
fdir2=fdir+fn+"\\"

#c_list
fn2="교수별_도구_클래스_리스트_2020_11_25.xlsx"
prof='인명훈' #교수님 이름
c_list=pd.read_excel(fdir+fn2, engine="openpyxl")
c_list=c_list.rename(columns=c_list.loc[0])
c_list=c_list.fillna(False)

#xml to dict
with open(fdir+fn+".xml",'r',encoding=('UTF8')) as fd:
    data = xmltodict.parse(fd.read())
with open(fdir1+fn1) as fd:
    label = xmltodict.parse(fd.read())

label=json.loads(json.dumps(label))
label=pd.DataFrame(label['ArrayOfLabelObject']['LabelObject'],columns=["name"])
data=json.loads(json.dumps(data))
#=json.loads(json.dumps(doc))

#label dict(name : c_max)
label=list(c_list['Tools Class Name'][2:])
c_max=list((c_list[prof][2:]))
for i in range(len(c_max)):
    if c_max[i]!=False:
        c_max[i]=1
label=dict(zip(label,c_max))

#list file naem, class name
name=[]
list_fn=[]
LabelItems=data['ListLabels']['lstItems']['LabelItems']
for i in range(len(LabelItems)):
    if LabelItems[i]['name']==None:
        continue
    list_fn.append(fn+"_{0:0>8}".format(LabelItems[i]['idx'])+".xml")
    name.append(LabelItems[i]['name']['string'])

#c_max
label['Graspers']=2
label['Trocar']=2
label['Curved Needle']=2
label['Robotic Needle Driver']=2

#count class name, annotation error  
class_dict={}
for c_name in label:
    if name.count(c_name)==0:
        continue
    sum=0
    for i in range(len(name)):
        if name[i].count(c_name)==0:
            continue
        if name[i].count(c_name)>label[c_name]:
            print('annotation error!!! : '+list_fn[i],c_name)
            continue
        sum+=name[i].count(c_name)
    #print(c_name, x.count(c_name))
    class_dict[c_name]=sum

#bbox error
for i in range(len(list_fn)):
    tree=ET.parse(fdir2+list_fn[i])
    root=tree.getroot()
    for bbox in root.iter('bndbox'):
        xmax,xmin=bbox.find('xmax').text,bbox.find('xmin').text
        ymax,ymin=bbox.find('ymax').text,bbox.find('ymin').text
        xmax,xmin,ymax,ymin=int(xmax),int(xmin),int(ymax),int(ymin)
        if (xmax-xmin)*(ymax-ymin)==0:
            print('bbox error!!! : '+list_fn[i])


#list(class_dict.keys())
#'Graspers' in name[i]