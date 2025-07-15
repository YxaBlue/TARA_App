import streamlit as st
# from lognavigation_bar import render_log_navbar

def render_loggedin_page():
    # render_log_navbar()
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url('https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752496796/Landing_Page_-_Logged_in_lbxa7y.png') no-repeat center center fixed;
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br><br><br><br><br><br><br><br><br><br><br>>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
    with col2:
        if st.button("FIND YOUR CAREER", key="career_btn"):
            st.session_state.page = "CST"  

    st.markdown("""
        <style>
            div[data-testid="stButton"] > button {
                position: relative;
                height: 70px;     
                width: 100%;       
                max-width: 400px;
                margin-top: 15px;  
                margin-left: 135px; 
                opacity: 0%;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
        <style>
            div[data-testid="stButton"]:nth-of-type(1) > button {
                transform: rotate(25deg);
            }
        </style>
    """, unsafe_allow_html=True) 