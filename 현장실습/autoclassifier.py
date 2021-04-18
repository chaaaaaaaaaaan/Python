# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:13:41 2021

@author: mteg_label3
"""

import os, shutil
import argparse
import pandas as pd
import xml.etree.ElementTree as ET


#argpaser 입력
parser=argparse.ArgumentParser()
parser.add_argument('--input_path', required=True, help='input_path내의 xml을 읽는다.')
parser.add_argument('--output_path', required=True, help='output_path 클래스별로 파일을 나눈다')
args=parser.parse_args()

#입력을 경로로 만듦
input_path=args.input_path+'\\'
output_path=args.output_path+'\\'

#label list
list_file='C:/Users/mteg_label3/Desktop/python/교수별_도구_클래스_리스트_2020_11_25.xlsx'
c_list=pd.read_excel(list_file, engine="openpyxl")
c_list=c_list.rename(columns=c_list.loc[0])
label=list(c_list['Tools Class Name'][2:])

#file list
file_list=os.listdir(input_path)#경로에있는 파일이름 읽어옴
xml_list=[]
for file in file_list:
    if '.xml' in file: xml_list.append(file[0:-4]) 

for c_name in label: 
    #class count
    sum=0    
    for xml in xml_list: 
        tree=ET.parse(input_path+xml+'.xml')
        root=tree.getroot()
        for name in root.iter('object'):
            sum +=(name.find('name').text).count(c_name)
 
    if sum !=0 : 
        #class 폴더 생성
        if os.path.isdir(output_path+c_name+'//')==False: os.mkdir(output_path+c_name+'//')
        #log에 입력    
        with open(output_path+c_name+'\\log.txt','wt',encoding='UTF8') as fd:
            fd.write(c_name+' '+str(sum)) 
    #copy
        for name in root.iter('object'):
            if name.find('name').text==c_name:
                shutil.copy(input_path+xml+'.xml', output_path+c_name+'\\'+xml+'.xml')
                shutil.copy(input_path+xml+'.png', output_path+c_name+'\\'+xml+'.png')
                  
print('Done')