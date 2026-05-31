import streamlit as st
import random
from time import sleep

st.title("Book Club")
st.subheader("Random book chosen from list")

uploaded_file = st.file_uploader("Upload a file with the books list", type=["csv"])

book = ""

lines = []
if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    lines = content.strip().splitlines()
    book = random.choice(lines)

    with st.spinner("Let's just make a small suspense...", show_time=True):
        sleep(5)

    st.write("The chosen book is: ")
    st.header(book)