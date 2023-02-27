import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
#import plotly.express as px
import os

st.subheader(":blue Education Details :open_book:")
st.write('\n')
study = {
    "Bachelor's": "St Mary`s College of Engineering and Technology ,Electrical  Engineering, (2015-2018)",
    "Diploma ": "Govt Polytechnic  college, (2012-2015)",
    "SSC": "Kakatiya High School, Nizamabad      (20011-2012)"  
}
cols = st.columns(len(study),gap="large")
for index, (name, details) in enumerate(study.items()):
    cols[index].success(f"{name}")
    cols[index].info(f"{details}")

 