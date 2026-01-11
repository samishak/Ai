import streamlit as st 
import pandas as pd
st.title("Streamlit text input")

name=st.text_input("enter your name")

age=st.slider("select your aeg :",100,20)

st.write(f"your age is ,{age}")
options=["python","java","C#"]

choice=st.selectbox("cjoose your fav language",options)
st.write(f"you selected {choice}")

if name:
    st.write(f"Hello,{name}")

data={
    "name":["john","sam","jake","kako"],
    "age":[28,19,28,38],
    "city":["ny","la","bei","tri"]
}

df=pd.DataFrame(data)
df.to_csv("sample data csv ")
st.write(df)

uploaded_file=st.file_uploader("choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
