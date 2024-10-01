import streamlit as st

enable_test = st.checkbox("Enable test")

enable = st.checkbox("Enable camera test 1234")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
