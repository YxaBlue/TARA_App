import streamlit as st

st.set_page_config(page_title="TARA", layout="wide")


#background
results_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://res.cloudinary.com/doddwukae/image/upload/v1752549276/RESULTS_qtfdcc.png);
        background-size: cover;
        background-position: center;
    }
    </style>
    """

st.markdown(results_bg, unsafe_allow_html=True)

# Define layout properties for customization
# Only display "CAREER" on the left and "80%" on the right, no details

# Display four careers on the left and their percentages on the right

careers = [
    ("CAREER 1", "80%"),
    ("CAREER 2", "75%"),
    ("CAREER 3", "65%"),
    ("CAREER 4", "60%")
]

# CSS for positioning
st.markdown("""
    <style>
    .career_left {
        position: fixed;
        top: 250px;
        left: 150px;
        color: black;
        font-size: 40px;
        font-weight: 700;
        z-index: 9999;
        line-height: 3;
    }
    .percent_right {
        position: fixed;
        top: 250px;
        left: 600px;
        color: black;
        font-size: 40px;
        font-weight: 700;
        z-index: 9999;
        line-height: 3;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

# HTML for careers and percentages
careers_html = '<div class="career_left">'
percents_html = '<div class="percent_right">'
for i, (career, percent) in enumerate(careers):
    careers_html += f"{career}<br>"
    percents_html += f"{percent}<br>"
careers_html += '</div>'
percents_html += '</div>'

st.markdown(careers_html, unsafe_allow_html=True)
st.markdown(percents_html, unsafe_allow_html=True)


# Job description details (modifiable variable for backend integration)
job_description = "Job Description details"

# CSS for job description positioning (no background)
st.markdown("""
    <style>
    .job_desc_box {
        position: fixed;
        top: 230px;
        left: 900px;
        width: 700px;
        color: #222;
        font-size: 22px;
        padding: 24px 32px;
        border-radius: 18px;
        z-index: 9999;
        box-shadow: none;
        background: none;
    }
    </style>
""", unsafe_allow_html=True)

# Display job description in styled box (no background)
st.markdown(f'<div class="job_desc_box">{job_description}</div>', unsafe_allow_html=True)


# Custom CSS for button positioning
st.markdown("""
    <style>
    .custom_button {
        position: fixed;
        bottom: 60px;
        right: 350px;
        z-index: 9999;
        padding: 16px 40px;
        font-size: 22px;
        font-weight: 700;
        cursor: pointer;
        opacity: 0;
    }
    .custom_button:hover {
        background: #005a9e;
    }
    </style>
""", unsafe_allow_html=True)

# Add a button using HTML to apply the custom class
st.markdown(
    '<button class="custom_button">Next</button>',
    unsafe_allow_html=True
)

