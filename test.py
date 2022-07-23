import streamlit as st
import os
st.write(os.getcwd())
os.system("python doFile.py")
str = open("data.txt")
st.write(str)

