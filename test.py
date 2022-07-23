import streamlit as st
import os
st.write(os.getcwd())
os.system("python doFile.py")
str = open("data.txt","r")
st.write(str.read())

