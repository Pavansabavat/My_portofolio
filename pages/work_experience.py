import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
#import plotly.express as px
import os

st.latex("Total Experience: 1  year")
st.write('\n')
st.write('\n')
x = st.button("Trainee   Experience")
if x==True:
    st.write("""
    :point_right: 1 year of Handson Experince  with Python coding  in Datascience   Projects
    """)
if x==True:
    st.balloons()
st.write('\n')
st.write('\n')
z = st.button("Internship")
if z==True:
    st.write("""
        :point_right: 1 years Internship in Nizam Deccan Sugar Limited , Nizamabad
        """
    )
    st.write(
        ":point_right: Selected for three months Data Science Internship at Innomatics Research Labs, Hyderabad."
    )
    st.snow()

