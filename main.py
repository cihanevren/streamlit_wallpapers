import reddit
from paginator import paginator
import streamlit as st
import functools
import operator
from PIL import Image
import os



urls = reddit.main()
image_filename = os.listdir(os.getcwd()+"/wallpapers")
#image_list = ['C:/Users/cihan/Desktop/GIT-REPS/streamlit_wallpapers/wallpapers/Desert Lights.png','C:/Users/cihan/Desktop/GIT-REPS/streamlit_wallpapers/wallpapers/Dark Boat.png', \
    #"C:/Users/cihan/Desktop/GIT-REPS/streamlit_wallpapers/wallpapers/Desert.png"]

image_list = []
for image in image_filename:
    image_list.append(Image.open(os.getcwd()+"/wallpapers/"+image))


for img in image_list:
    #print(img.mode)
    if img.mode != 'RGB':
        img_fname = img.filename.split('/')[-1]
        #print(img.filename)
        img = img.convert('RGB')
        img.save(img_fname)

#for img in image_list:
    #print(img.size)

#image = Image.open('C:/Users/cihan/Desktop/GIT-REPS/streamlit_wallpapers/wallpapers/Desert Lights.png')

#posts = functools.reduce(operator.iconcat, posts, [])

col1, col2, col3 = st.columns(3)

with col1:
    for i in image_list[::3]:
        st.image(i, caption=i.filename.split('/')[-1][:-4])
        st.checkbox("click", key='dynamic_checkbox_' + str(i.filename.split('/')[-1][:-4]))

with col2:
    for i in image_list[1:-1:3]:
        st.image(i, caption=i.filename.split('/')[-1][:-4])
        st.checkbox("click", key='dynamic_checkbox_' + str(i.filename.split('/')[-1][:-4]))

with col3:
    for i in image_list[2:-1:3]:
        st.image(i, caption=i.filename.split('/')[-1][:-4])
        st.checkbox("click", key='dynamic_checkbox_' + str(i.filename.split('/')[-1][:-4]))

def get_selected_checkboxes():
    return [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]
st.write('You selected:')
st.write(get_selected_checkboxes())

# for img in get_selected_checkboxes():

#     st.download_button(label)

st.write('HEREIS ANOTHER SECTION')

col4, col5, col6, col7 = st.columns(4)

with col4:
    st.write('SECTION 1')

with col5:
    st.write('SECTION 2')

with col6:
    st.write('SECTION 3')

with col7:
    st.write('SECTION 4')
# print(my_list)
# image_iterator = paginator("Select Page", image_list, items_per_page=20)
# indices_on_page, images_on_page = map(list, zip(*image_iterator))
# st.image(images_on_page, width=222, caption=indices_on_page)
# st.checkbox("click", key=indices_on_page)




#st.image(image_list, width=300)
#image_list[0].show()