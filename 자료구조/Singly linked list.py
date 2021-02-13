# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:49:32 2021

@author: skukm
"""

class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Slinkedlist(object):
    def __init__(self):
        self.head=None
        self.count=0
    
    def size(self):
        return self.count
    
    def append(self, data):
        if self.head==None:
            self.head=Node(data)
        else:
            cur=self.head
            while cur.next !=None:
                cur=cur.next
            cur.next=Node(data)
        self.count+=1
                
    def insert(self, data, idx):
        cur=self.head
        prev=None
        cur_i=0
        if idx==0:
            if self.head != None:
                next=self.head
                self.head=Node(data)
                self.head.data=next
            else:
                self.head=Node(data)
        else:
            while cur_i<idx:
                if cur != None:
                    prev=cur
                    cur=cur.next
                else:
                    break
                cur_i+=1
            if cur_i==idx:
                Node(data).next=cur
                prev.next=Node(data)
            else:
                return -1
        self.count+=1
        
    def delete(self, idx):
        cur=self.head
        prev=None
        cur_i=0
        next=self.head.next
        if idx==0:
            self.head=next
        else:
            while cur_i<idx:
                if cur.next != None:
                    prev=cur
                    cur=next
                    next=next.next
                else:
                    break
                cur_i +=1
            if cur_i==idx:
                prev.next=next
            else:
                return -1
        self.count-=1
    
    def print(self):
        cur=self.head
        string=""
        while cur != None:
            string += str(cur.data)
            if cur.next != None:
                string += "->"
            cur=cur.next
        print(string)
        
sl=Slinkedlist()