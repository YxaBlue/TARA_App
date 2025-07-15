import streamlit as st
# from navigation_bar import render_navbar

st.set_page_config(page_title="TARA", layout="wide")

def render_landing_page():

    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752483561/Landing_Page_-_New_User_goipfc.png);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """

    # render_navbar()
    st.markdown(page_bg_img, unsafe_allow_html=True)