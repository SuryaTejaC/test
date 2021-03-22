import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.text_input('user name')
filename=st.file_uploader("Upload Files",type=['csv'])
click=st.button('submit')
if click==True:
        df=pd.read_csv(filename)
        st.text('Output 1')
        st.write(df.head())
        st.text('Output 2')
        fig=plt.figure()
        figure=plt.subplot(2,2,2)
        sns.scatterplot(data = df, x = "petal_length", y = "sepal_length")
        st.write(fig)
