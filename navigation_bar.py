import streamlit as st

def render_Newuser_NavBar():
    st.markdown(
        """
        <style>
            .stButton { margin-top: -60px; }
            .stButton > button, st.Button button, .stButton {
                margin-left: 470px;
                opacity: 0;
            }
        </style>
        <div style= "width: 100vw; position: fixed; top: 20px; left: 215px; z-index: 0; display: flex; justify-content: center;">
            <div style= "position: relative; width: 90%;">
                <img src='https://res.cloudinary.com/doddwukae/image/upload/v1752548698/Menu_xlsgit.png' style= 'width= 100%; display: block;'>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 2, 2])
    with col1:
        if st.button("About Us", key= "AboutUs_btn", help="About Us", use_container_width= True):
            st.session_state.page = "about_us"
    
    with col5:
        if st.button("LOG IN/SIGN UP", key= "Login_btn", help="LOG IN/SIGN UP", use_container_width= True):
            st.session_state.page = "login"

