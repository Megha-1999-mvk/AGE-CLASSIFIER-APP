import streamlit as st
st.title("age classifier app")
age=st.slider("select your age",0,100)
if 0<=age<=12:
    category="CHILD..."
elif 13<=age<=19:
    category="TEENAGER"
else:
    category="ADULT..."
st.write(category)
