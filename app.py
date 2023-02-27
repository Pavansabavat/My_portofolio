import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
#import plotly.express as px
import os

# path of the picture
base_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
image_ = base_dir / "resources" / "pavan.jpg"
img = Image.open(image_)
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(img, width=300)
with col2: 
    st.subheader("S.Pavan Kumar ")
    st.write("""
        To be associated with a progressive organization that 
        gives me scope to apply my knowledge and skils to work
        towards the growth of the organization and me.
    """)
    st.write("""
             :pushpin: Data science Intern | Data Science Enthusiast 
             """)
    st.write("""Sabavatpavankumar1@gmail.com
            """)
st.write("Follow me on:")
st.write(":link: https://www.linkedin.com/in/pa1-330719244/")
st.write(":link: https://github.com/Pavansabavat")
