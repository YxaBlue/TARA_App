import streamlit as st

def render_LoggedIn_NavBar():
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
                <img src='https://res.cloudinary.com/doddwukae/image/upload/v1752551244/Menu_afytx6.png' style= 'width= 100%; display: block;'>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 2, 2])
    with col1:
        if st.button("About Us", key= "AboutUs_btn", help="About Us", use_container_width= True):
            st.session_state.page = "about_us"
    
    with col5:
        if st.button("JUAN DE LA CRUZ", key= "user_profile", help="User Profile", use_container_width= True):
            st.session_state.page = "user_profile"

