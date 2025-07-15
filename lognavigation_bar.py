import streamlit as st

def render_LoggedIn_NavBar():
    st.markdown( """
        <style>
            .stButton { margin-top: -67px; }
            .stButton > button, st.Button button, .stButton {
                opacity: 0 !important;
            }
        </style>
        <div style= "width: 100vw; position: fixed; top: 20px; left: 0; z-index: 0; display: flex; justify-content: center;">
            <div style= "position: relative; width: 90%;">
                <img src='https://res.cloudinary.com/doddwukae/image/upload/v1752548698/Menu_xlsgit.png' style= 'width= 100%; display: block;'>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns([20, 4, 1, 4, 1])
    with col4:
        if st.button("LOG IN/SIGN UP", key= "Login_btn", help="LOG IN/SIGN UP", use_container_width= True):
            st.session_state.page = "Login/Signup"
