# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:53:47 2024

@author: Arslan Shahid
"""
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import plotly.express as px

import plotly.graph_objects as go
import streamlit as st


#writing streamlit 


def make_sankey(source,target,values=[], title='Sankey Diagram'):
    if len(values) ==0:
        values = [1 for i in range(len(source))]
    
    fig = go.Figure(data=[go.Sankey(
#Basic styling options
    node = dict(
    pad = 15,
    thickness = 20,#Tells the width of the node
    line = dict(color = 'black', width = 0.5),#Node border settings
    #(width & color)
    color = 'blue' #Node color 
    ),
    #Main attributes are the lists, if you have these figured out you #can make a Sankey.
    link = dict(
    source = source,#Contains info of origin of link
    target = target,#Contains info about which link to join
    value = values#Contains relative sizes(width) of links
    ))])
    #Adding a title & showing the figure (Optional)
    fig.update_layout(title_text=title, font_size=10)
#     fig.show()
    return fig


def make_source_target(n,l):
    matrix = np.random.randint(n, size=(3, l))
    return matrix[0],matrix[1],matrix[2]


# help(pd.qcut(df['Pay'], 5).iloc[0])

def aggregator(df,col1,col2):
#     print(col1,col2)
    x = list(df.columns)
    if len(x)<=2:
        
        return  df.groupby([col1,col2]).agg('count').reset_index()
    # [[col1,col2,x[0]]]
    x.remove(col1)
    x.remove(col2)
    return df.groupby([col1,col2]).agg('count').reset_index()[[col1,col2,x[0]]]


# df['Pay-Band'].unique()
def make_data(df,columns):
    iterations = len(columns)
    names = []
    count_dict = {} #will contain all info of value list
    source_list = [] #will contain all info of source
    target_list = []
    # data_values ={}
    if iterations>2:
        
        for i in range(iterations-1):
            temp = aggregator(df,columns[i],columns[i+1])

            temp.columns = [columns[i],columns[i+1],'counts']
            for x,y,z in zip(temp[columns[i]],temp[columns[i+1]],temp['counts']):
                source_list.append(x)
                target_list.append(y)
                count_dict[x+'-'+y] = z

    elif iterations==2:
        
        temp = aggregator(df,columns[0],columns[1])
        # temp.columns = [columns[0],columns[1],'counts']
        for x,y in zip(temp[columns[0]],temp[columns[1]]):
            source_list.append(x)
            target_list.append(y)
            count_dict[x+'-'+y] = 1
    else:
        return False
    num =0
    for i in source_list:
        if i not in names:
            names.append(i)
            num+=1
    for i in target_list:
        if i not in names:
            names.append(i)
            num+=1
    all_numerics = {i:y for i,y in zip(names,range(len(names)))}
    source = [all_numerics[x] for x in source_list]
    target = [all_numerics[x] for x in target_list]
        
        
    
    
    

        
    return {'source_list':source_list,'target_list':target_list,'count_dict':count_dict,'source':source,'target':target,'all_numerics':all_numerics}

def make_node(color ='black',line =dict(), labels=[]):
    if len(line) == 0:
        line = dict()
    n = dict(
            pad = 15,
            thickness = 20,#Tells the width of the node
            line = line,#Node border settings
            label = labels,
            # font_size=25,
            #(width & color)
            color = color #Node color 
              )
    return n


def update_node(fig,color=None):
    if color!= None:
        fig.data[0]['node']['color'] = color

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    

    

def make_sankey(data, node = dict(),title='Basic Sankey',link_color = 'rgba(111, 112, 112,0.5)'):
    if len(node)==0:
        node = make_node()
    fig = go.Figure(data=[go.Sankey(
#Basic styling options
    node = node,
    #Main attributes are the lists, if you have these figured out you #can make a Sankey.
    link = dict(
    source = data['source'],#Contains info of origin of link
    target = data['target'],#Contains info about which link to join
    value = [data['count_dict'][x+'-'+y] for x,y in zip(data['source_list'],data['target_list'])], #Contains relative sizes(width) of links
    color = [link_color for i in range(len(data['source']))]
    ))])
    #Adding a title & showing the figure (Optional)
    fig.update_layout(title_text=title, font_size=15)
#     fig.show()
    return fig

def assign_job(x):
    r = np.random.randint(100)
    if r >0 and r<=30:
        return 'Data Scientist'
    elif r>30 and r<=90:
        return 'Data Analyst'
    else:
        return 'Research Scientist'
    
def assign_industry(job):
    r = np.random.randint(100)
    if job =='Data Scientist':
        if r >0 and r<=30:
            return 'Consulting'
        elif r>30 and r<=90:
            return 'Technology'
        else:
            return 'Finance'
    elif job =='Data Analyst':
        if r >0 and r<=30:
            return 'Technology'
        elif r>30 and r<=90:
            return 'Consulting'
        else:
            return 'Finance'
    else:
        return 'Technology'
    
def assign_sex(x):
    r = np.random.randint(100)
    if r<50:
        return 'Male'
    else:
        return 'Female'
def assign_age(x):
    return str(np.random.randint(15) + 25)+' yr'
        

def assign_pay(job,industry):
    job_multiplier = {'Data Scientist':2, 'Data Analyst':1, 'Research Scientist':3}
    industry_multiplier = {'Technology':2, 'Consulting':1.9, 'Finance':4}
    return 1000*(30+np.random.randint(10)*job_multiplier[job]*industry_multiplier[industry]-np.random.randint(4))

def highest_education(job):
    r = np.random.randint(100)
    if job =='Data Scientist':
        if r >0 and r<=70:
            return 'Bachelors'
        elif r>70 and r<=90:
            return 'Masters'
        else:
            return 'PhD'
    elif job =='Data Analyst':
        if r >0 and r<=90:
            return 'Bachelors'
        else:
            return 'Masters'
    else:
        return 'PhD'





