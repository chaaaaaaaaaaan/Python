# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:13:41 2021

@author: mteg_label3
"""

import os
import argparse
import xml.etree.ElementTree as ET


parser=argparse.ArgumentParser()
parser.add_argument('--path', required=True, help='파일 경로를 입력하시오')
#파일만 변경
parser.add_argument('--fn', required=False, help='파일 이름을 입력하시오')
parser.add_argument('--name1', required=True, help='변경될 class를 입력하시오')
parser.add_argument('--name2', required=True, help='변경할 class를 입력하시오')
args=parser.parse_args()

file_list=os.listdir(args.path)
xml_list=[]
for file in file_list:
    if '.xml' in file: xml_list.append(file)

if args.fn!=None:
    xml_list=[args.fn]
    
for xml in xml_list: 
    with open(args.path+'\\'+xml,'rt',encoding=('UTF8')) as fd:
        tree=ET.parse(fd)
        root=tree.getroot()
        for name in root.iter('object'):
            class_name=name.find('name').text
            if class_name==args.name1:
                name.find('name').text=args.name2
        tree.write(args.path+'\\'+xml)
       
