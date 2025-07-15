import streamlit as st
# from lognavigation_bar import render_log_navbar

st.set_page_config(page_title="TARA", layout="wide")

def render_career_suitability_page():
    # render_log_navbar()
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752499464/CST_l7wvfz.png);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("<br><br><br>>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])  

    with col2:
        uploaded_file = st.file_uploader(
            "", 
            type=["pdf"], 
            accept_multiple_files=False, 
            label_visibility="collapsed"
        )

    with col2:
        if st.button("ANALYZE"):
            if uploaded_file:
                st.session_state.page = "Assessment"  

    st.markdown("""
    <style>
        div[data-testid="stFileUploader"] {
            width: 100% !important;
            min-height: 300px !important;   
            padding: 2rem 1rem !important;
            overflow: hidden !important;  
            opacity: 0%;
        }
        div[data-testid="stFileUploader"] svg {
            width: 480px !important;       
            height: 480px !important;
        }
        div[data-testid="stFileUploader"] label {
            font-size: 1.5rem !important;
        }
            div[data-testid="stButton"] > button {
            position: relative;
            height: 70px;     
            width: 100%;       
            max-width: 600px;
            margin-top: -100px;  
            margin-left: 25px; 
            opacity: 0%;
        }
    </style>
    """, unsafe_allow_html=True)

    if uploaded_file:
        st.markdown("""
            <style>
                div[data-testid="stFileUploader"] ul {
                    display: none !important;
                }
            </style>
        """, unsafe_allow_html=True)