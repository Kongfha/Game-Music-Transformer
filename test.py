import streamlit as st
import os
st.write(os.getcwd())
os.system("python doFile.py")
str = open("data.txt")
th_split = str.splitlines()
st.write(th_split[0])

