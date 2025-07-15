import streamlit as st
from navigation_bar import render_Newuser_NavBar

def render_landing_page():
    st.set_page_config(page_title="TARA", layout="centered")
    landing_page_background_img = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-image: url(https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752483561/Landing_Page_-_New_User_goipfc.png);
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
    """
    render_Newuser_NavBar()
    st.markdown(landing_page_background_img, unsafe_allow_html=True)


render_landing_page()