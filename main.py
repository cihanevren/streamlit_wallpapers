import reddit
import paginator
import streamlit as st
import functools
import operator

posts = reddit.main()


posts = functools.reduce(operator.iconcat, posts, [])

# print(my_list)
#image_iterator = paginator("Select Page", ['https://i.redd.it/a987r21195871.png','https://i.imgur.com/0t7byMT.jpg'])
# indices_on_page, images_on_page = map(list, zip(*image_iterator))
# st.image(images_on_page, width=222, caption=indices_on_page)


st.image(posts,width=300)