import streamlit as st

st.title("Hello World")
clicked = st.button("Click me")

if clicked:
    st.write("Clicked!")
