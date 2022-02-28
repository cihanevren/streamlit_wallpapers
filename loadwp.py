from paginator import paginator
import streamlit as st
import os
from PIL import Image
import numpy as np

list_dir = os.listdir(r'C:\Users\cihan\wallpapers')
# list_dir

# list_dir[1]

image_path = [r"C:/Users/cihan/wallpapers/"  + path_name for path_name in list_dir]

# #def load_image(img):
#     im = Image.open(img)
#     image = np.array(im)
#     return image

#uploadFile = st.file_uploader("C:\z3_workenv\wallpapers\A Trip Through the Forest.png", type=['jpg', 'png'])

#img = load_image(uploadFile)
st.image("https://i.redd.it/quhvjxji0k571.jpg",width=400)

st.image("https://i.redd.it/e7ud22ig2h871.jpg",width=250)
st.write("Image Uploaded Successfully")
# image_path

# [path_name for path_name in list_dir]

# image_iterator = paginator("Select a sunset page", images)
# indices_on_page, images_on_page = map(list, zip(*image_iterator))
# st.image(images_on_page, width=100, caption=indices_on_page)



# from matplotlib.pyplot import imshow
# import numpy as np
# from PIL import Image


# pil_im = Image.open(image_path[0], 'r')
# imshow(np.asarray(pil_im))

# from PIL import Image
# import numpy as np
# from skimage import io