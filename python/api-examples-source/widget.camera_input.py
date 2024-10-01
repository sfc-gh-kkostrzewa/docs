import streamlit as st



enable = st.checkbox("Enable camera test 6")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
