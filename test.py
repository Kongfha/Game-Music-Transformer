import streamlit as st
import os
st.write(os.getcwd())
os.system("python doFile.py")
str = open("data.txt")
th_split = a_file_contents.splitlines()
st.write(th_split[0])

