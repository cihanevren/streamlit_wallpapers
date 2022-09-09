import reddit
from paginator import paginator
import streamlit as st
import functools
import operator
from PIL import Image
import os
from urllib.request import urlopen
import requests


from imageio import imread
#img = imread('https://i.redd.it/uosafjoc95l91.png')


img = "https://i.redd.it/uosafjoc95l91.png"

r = requests.get(img, stream = True)
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
st.write("HERE IS YOUR IMAGE")
st.image("https://i.redd.it/uosafjoc95l91.png", caption='that is the image')
#img = Image.open(urlopen("https://i.redd.it/uosafjoc95l91.png"))
button = st.download_button("download the image", data=r, mime="image/jpeg", file_name="image.jpeg")

if button:
    st.write("You just clicked the download button")

