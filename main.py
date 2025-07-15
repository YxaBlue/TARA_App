import streamlit as st
from landing_page import render_landing_page
from login_page import render_login_page
from loggedin_page import render_loggedin_page
from CST_page import render_career_suitability_page
from assessment_page import render_assessment_page
from test_page import render_test_page
from results_page import render_results_page
# from upskilling_page import render_upskilling_page

st.set_page_config(page_title="TARA", layout="wide")

# Default page
if "page" not in st.session_state:
    st.session_state.page = "landing"

if st.session_state.page == "landing":
    render_landing_page()
elif st.session_state.page == "login":
    render_login_page()
elif st.session_state.page == "loggedin":
    render_loggedin_page()
elif st.session_state.page == "CST":
    render_career_suitability_page()
elif st.session_state.page == "Assessment":
    render_assessment_page()
elif st.session_state.page == "Test":
    render_test_page()
elif st.session_state.page == "Results":
    render_results_page()
# elif st.session_state.page == "Upskill":
#     render_upskilling_page()