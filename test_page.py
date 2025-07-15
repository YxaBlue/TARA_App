import streamlit as st
# from lognavigation_bar import render_log_navbar

st.set_page_config(page_title="TARA", layout="wide")

def render_test_page():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752508159/Job_Assessment_uabogp.png);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """

    # render_log_navbar()
    st.markdown(page_bg_img, unsafe_allow_html=True)


    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Madimi+One&display=swap');
    div[data-testid="stButton"] > button {
        width: 60% !important;
        min-width: 10px !important;
        height: 70px !important;
        font-size: 1.1rem !important;
        margin: 0 auto;
        margin-top: -30px;   
        margin-left: 220px; 
        display: block;
        opacity: 0;
        }
    .madimi-sample {
        font-family: 'Madimi One', cursive !important;
        color: #726767 !important;
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
        margin-left: -12rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
<style>
    div[data-testid='stTextInput'] {
        width: 100% !important;       
        min-width: 1000px !important;   
        margin: 0 auto 30px auto !important; 
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
</style>
""", unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)  

    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        st.markdown("<div class='madimi-sample'>Question 1: 1+1?</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        answer1 = st.text_input("", key="answer1", placeholder="ANSWER")
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        st.markdown("<div class='madimi-sample'>Question 2: 1+1?</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 45px;'></div>", unsafe_allow_html=True)
        answer2 = st.text_input("", key="answer2", placeholder="ANSWER")
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        st.markdown("<div class='madimi-sample'>Question 3: 1+1?</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 45px;'></div>", unsafe_allow_html=True)
        answer3 = st.text_input("", key="answer3", placeholder="ANSWER")
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        finish_btn = st.button("FINISH", key="finish_btn", use_container_width=True)
        if finish_btn:
            st.session_state.page = "Results"  
