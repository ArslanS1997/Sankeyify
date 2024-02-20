# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:51:25 2024

@author: Arslan Shahid
"""
import pandas as pd
import numpy as np
from PIL import Image
import sankey_methods as sm
import plotly.graph_objects as go


import streamlit as st
from streamlit_extras.app_logo import add_logo


# def stop_func():
#     stop = True
    
# def display_plot():
    
def change_fig_color(c):
    st.sesion_state.plotly_fig.data[0]['node']['color'] = c



def plot_func(c_size,df):
    data=sm.make_data(df[c_size],c_size)
    
    fig = sm.make_sankey(data, node=sm.make_node(color='rgba(3, 211, 252,0.7)', labels = list(data['all_numerics'].keys())))
    # st.plotly_chart(fig,use_container_width=True)
    return fig



def update_node_color(fig, color):
    fig.data[0]['node']['color'] = color
    return fig


#writing streamlit 

st.set_page_config(layout="wide")
if 'fig' not in st.session_state:
    st.session_state['fig'] = None
    
# if 'edit_option' not in st.session_state:
#     st.session_state['edit_option'] =
# len_df =100000
with st.sidebar:
    st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #73a3ef;
    }
</style>
""", unsafe_allow_html=True)
    image = Image.open('Full Text Logo Small.png')
    st.image(image,width=350)
    # st.markdown("![](C:\\Users\\Arslan Shahid\\Desktop\\Firebird Technologies\\Sankeyify\icon.png)", unsafe_allow_html=True)

  # 
st.write('Welcome to Sankeyify - Please begin by uploading a dataset in this [format](www.uploadsomething.com)')
df = pd.DataFrame()
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    # st.write(df)

    st.write(df.head(10))

    c = list(df.select_dtypes(exclude=['int64','float64','bool']).columns)
    options = st.multiselect(
        'Select the columns. you need upto 5',c,max_selections = 5
       )
    
    
    # st.write(print(options))
    # st.write(help(options))
    
    c_size_dict = {i:len(df[i].unique()) for i in options}
    
    st.write('You selected, ****(Remember for best ploting results only pick those columns with less than 25 categories)****:', c_size_dict)
    
    if 'Plot' not in st.session_state:
        st.session_state.Plot = False
    if 'edit_option' not in st.session_state:
        st.session_state.edit_option = False
    if 'plotly_fig' not in st.session_state:
        st.session_state.plotly_fig = go.Figure()
    if 'color' not in st.session_state:
        st.session_state.color = sm.rgb_to_hex(3, 211, 252)
    # if 'data' not in st.session_state:
    #     st.session_state.color = sm.rgb_to_hex(3, 211, 252)
    
    c_size = list(c_size_dict)
    
    
    
    st.write(df[c_size].head(10))
    # bool_ = False
    
    default_color = sm.rgb_to_hex(3, 211, 252)
    
    plot = st.button('Plot', key='Plot')
    plot_spot = st.empty()
    edit_option = st.selectbox(
    'Select which property you would like to edit',('Node','Link','Layout'), key='edit_option')
    color=st.color_picker('Pick A Color',default_color, on_change=change_fig_color)
    if plot:
        with plot_spot:
            data = sm.make_data(df[c_size],c_size)
            fig = sm.make_sankey(data, sm.make_node(color=default_color))
            plotly_fig = st.plotly_chart(fig,use_container_width=True, key='plotly_fig')


            
            
            
        
    
 
    
        
    
        