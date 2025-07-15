import streamlit as st
# from navigation_bar import render_navbar

def render_login_page():
    # render_navbar()
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url('https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752495671/Sign_up_page_q9cg1k.png') no-repeat center center fixed;
                background-size: cover;
            }}

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
            /* Reduce space between Streamlit input widgets */
            div[data-testid="stTextInput"] {
                margin-top: -0.5rem !important;
                margin-bottom: -0.9rem !important;
                border: none !important;
                box-shadow: none !important;
                background: transparent !important;
            }
            div[data-testid="stTextInput"] input {
                background-color: #fff !important;
                border-radius: 0 !important;
                border: none !important;
                outline: none !important;
                color: #000 !important;
            }
            div[data-testid="stButton"] > button {
                width: 100% !important;
                max-width: 280px;
                margin-left: 115px;
                display: block;
                height: 50px !important;        
                border-radius: 1.5rem !important;
                margin-top: 12px !important;   
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        email = st.text_input("", key="login_email")
        password = st.text_input("", type="password", key="login_password")
        st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
        login_btn = st.button("Log In", key="login_btn_main")
        if login_btn:
            if email == "hackit@gmail.com" and password == "123":
                st.session_state.page = "loggedin"
            elif email == "" and password == "":
                st.session_state.page = "loggedin"
            else:
                st.error("Invalid email or password.")