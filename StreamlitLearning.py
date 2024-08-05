import streamlit as st
import pandas as pd
from PIL import  Image
import numpy as np

st.title("Welcome to Machine learning Tutorial using Streamlit by Blossom")
st.header("This is the header")
st.text(" this is some text")
st.write("we are going there")
image = Image.open("blossom.jpeg")
Resize_image =image.resize((300,300))

st.image(Resize_image, caption="This is an image")

st.markdown(" this a markdown header")

data = {
     "col 1": [1,2,3,4,5,6,7],
     "col 2": [8,9,10,11,12,13,14]
}

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

# chart_value = pd.DataFrame(
#     np.random.randn(10, 4),
#     columns= ['a','b','c','d']
# )
# st.line_chart(chart_value)
# st.bar_chart(chart_value)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50,50] + [37.75, -122.4],
#     columns=['lat', 'lon']
# )
#
# st.map(map_data)
with st.container():
    st.write(" this is a container")

    age = st.slider('select your age', 0, 100, 10)
    st.write('your age is:', age)

    name = st.text_input('enter your name')
    st.write('Hello ', name)


st.write("outside the container")


if st.checkbox("Show/Hide"):
    st.text("showing")
    st.write('you click on showing')

gender = st.radio('Gender', ['Male', 'Female'])
status = st.radio('Select your status', ('Good', 'Bad'))

if status == 'Good':
    st.success('Your are Good')
    st.write('Be good')
else:
    st.warning('You are bad')
    st.write('you are bad!')

box = st.selectbox('select your favorite programming language', ['Ptyhon', 'C#', 'Java', 'C++'])
st.write('you selected', box)

box2 = st.multiselect('Select your favourite fruit', ['mango','banana', 'pineaple', 'orange'])
st.write('you selected:', box2)

options = st.multiselect("Select your favorite fruits", ['Apple', 'Banana', 'Orange'])
st.write("You selected:", options)

st.sidebar.title("Side bar title")
st.sidebar.write("Good Morning blossom")

sideOption = st.sidebar.selectbox("choose a number",
                                  list(range(1,11)))

st.sidebar.write(sideOption)

sideOption2 = st.sidebar.selectbox("pick a number", [1,2,3,4,5,6])
st.sidebar.write(sideOption2)

col1, col2, col3 = st.sidebar.columns(3)

with col1:
    st.sidebar.title("Header 1")
    st.sidebar.write("Content in col 1")

with col2:
    st.sidebar.title("Header 2")
    st.sidebar.write("Content in col 2")

with col3:
    st.sidebar.title("Header 3")
    st.sidebar.write("Content in col 3")

with st.expander("See explanation"):
    st.write(" This is an expander ...... i am greatfull for how i am learning ML and AI")

tab1, tab2, tab3 = st.tabs(['Tab 1','Tab 2', 'Tab 3'])

with tab1:
    st.header(" this is tab 1")
    st.write("Welcome")

with tab2:
    st.header(" this is tab 2")
    st.write("we are getting there")

with tab3:
    st.header(" this is tab 3")
    st.write(" where have you being")

image = Image.open("blossom.jpeg")
Resize_image =image.resize((300,300))

st.image(Resize_image, caption="This is an image")