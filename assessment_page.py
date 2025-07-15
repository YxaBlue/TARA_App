import streamlit as st
# from lognavigation_bar import render_log_navbar

def render_assessment_page():
    # render_log_navbar()
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url('https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752502613/CST_1_jt0szv.png') no-repeat center center fixed;
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # State for selected career
    if 'selected_career' not in st.session_state:
        st.session_state.selected_career = None

    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown("<div style='height: 225px;'></div>", unsafe_allow_html=True)
        if st.button("", key="career1", use_container_width=True):
            st.session_state.selected_career = "career1"
        st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
        if st.button("", key="career2", use_container_width=True):
            st.session_state.selected_career = "career2"
        st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
        if st.button("", key="career3", use_container_width=True):
            st.session_state.selected_career = "career3"
        st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
        if st.button("", key="career4", use_container_width=True):
            st.session_state.selected_career = "career4"
    with col2:
        st.markdown("<div style='height: 639px;'></div>", unsafe_allow_html=True)
        if st.button("TAKE ASSESSMENT", key="take_assessment", use_container_width=True):
            if st.session_state.selected_career is not None:
                st.session_state.page = "Test"  

    st.markdown("""
        <style>
            div[data-testid="stColumn"]:first-child div[data-testid="stButton"] > button {
                margin-left: 500px !important;
                position: relative;
                height: 70px;     
                width: 100%;       
                max-width: 200px;
                margin-top: 15px;  
                margin-left: 135px; 
                opacity: 0%;
            }
            div[data-testid="stColumn"]:nth-child(2) div[data-testid="stButton"] > button {
                margin-left: 200px !important;  
                position: relative;
                height: 60px;     
                width: 100%;       
                max-width: 400px;
                margin-top: 25px;  
                margin-left: 135px; 
                opacity: 0%;
            }
        </style>
    """, unsafe_allow_html=True)