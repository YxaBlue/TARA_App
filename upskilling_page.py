import streamlit as st

st.set_page_config(page_title="TARA", layout="wide")

#background
upskill_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752510189/Upskilling_Page_wbmzkr.png);
        background-size: cover;
        background-position: center;
    }
    </style>
    """

st.markdown(upskill_bg, unsafe_allow_html=True)

# Define lists for dynamic text
skills = [
    ("Python", "Details about Python..."),
    ("Basic Cybersecurity", "Details about..."),
    ("HTML", "Details about..."),
    ("AWS", "Details about..."),
    ("Cloud Computing", "Details about..."),
    ("Data Structure", "Details about...")
]

# Split into left and right columns
left_skills = skills[:3]
right_skills = skills[3:]

# Display left column (left: 150px)
for i, (skill_text, details_text) in enumerate(left_skills):
    top_skill = 230 + i * 150
    top_details = top_skill + 70

    st.markdown(f"""
        <style>
        .skill_left{i} {{
            position: fixed;
            top: {top_skill}px;
            left: 150px;
            color: black;
            font-size: 40px;
            font-weight: 700;
            z-index: 9999;
        }}
        .details_left{i} {{
            position: fixed;
            top: {top_details}px;
            left: 150px;
            color: black;
            font-size: 20px;
            font-weight: 500;
            z-index: 9999;
        }}
        </style>
        <div class="skill_left{i}">{skill_text}</div>
        <div class="details_left{i}">{details_text}</div>
    """, unsafe_allow_html=True)

# Display right column (left: 800px)
for i, (skill_text, details_text) in enumerate(right_skills):
    top_skill = 230 + i * 150
    top_details = top_skill + 70

    st.markdown(f"""
        <style>
        .skill_right{i} {{
            position: fixed;
            top: {top_skill}px;
            left: 800px;
            color: black;
            font-size: 40px;
            font-weight: 700;
            z-index: 9999;
        }}
        .details_right{i} {{
            position: fixed;
            top: {top_details}px;
            left: 800px;
            color: black;
            font-size: 20px;
            font-weight: 500;
            z-index: 9999;
        }}
        </style>
        <div class="skill_right{i}">{skill_text}</div>
        <div class="details_right{i}">{details_text}</div>
    """, unsafe_allow_html=True)
