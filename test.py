import reddit
from paginator import paginator
import streamlit as st
import functools
import operator
from PIL import Image
import os

@st.experimental_memo(suppress_st_warning=True)
def get_urls():
    st.write("HERE IS YOUR IMAGE")
    st.image("https://i.redd.it/uosafjoc95l91.png", caption='that is the image')
    print("I RAN THIS ONLY ONCE")
    urls_raw = reddit.main()
    urls = [i for i in urls_raw if str(i) != "None"]
    return urls


urls = get_urls()

col1, col2, col3 = st.columns(3)

with col1:
    for i in urls[::3]:
        st.image(i, caption="image")
        st.checkbox("click", key="checkbox_" + str(i))

with col2:
    for i in urls[1:-1:3]:
        st.image(i, caption="image")
        st.checkbox("click", key="checkbox_" + str(i))

with col3:
    for i in urls[2:-1:3]:
        st.image(i, caption="image")
        st.checkbox("click", key="checkbox_" + str(i))



def get_selected_checkboxes():
    return [i.replace('checkbox_','') for i in st.session_state.keys() if i.startswith('checkbox_') and st.session_state[i]]


col4, col5 = st.columns(2)

with col4:

    st.write('You selected:')
    st.write(get_selected_checkboxes())

with col5:
    st.write("Download Section")


    for img in get_selected_checkboxes():
        with open(img, "rb") as file:

            st.download_button("Download Button", file)
# if 'dummy_data' not in st.session_state.keys():
#     dummy_data = ['IND','USA','BRA','MEX','ARG']
#     st.session_state['dummy_data'] = dummy_data
# else:
#     dummy_data = st.session_state['dummy_data']

# def checkbox_container(data):
#     st.header('Select A country')
#     new_data = st.text_input('Enter country Code to add')
#     cols = st.columns(10)
#     if cols[0].button('Add Coutry'):
#         dummy_data.append(new_data)
#     if cols[1].button('Select All'):
#         for i in data:
#             st.session_state['dynamic_checkbox_' + i] = True
#         st.experimental_rerun()
#     if cols[2].button('UnSelect All'):
#         for i in data:
#             st.session_state['dynamic_checkbox_' + i] = False
#         st.experimental_rerun()
#     for i in data:
#         st.checkbox(i, key='dynamic_checkbox_' + i)

# def get_selected_checkboxes():
#     return [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]


# checkbox_container(dummy_data)
# st.write('You selected:')
# st.write(get_selected_checkboxes())