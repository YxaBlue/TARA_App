import PyPDF2
import openai
import json
import re

# to call AI
client = openai.OpenAI(api_key = "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")

# extract text from PDF file
def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        return " ".join(page.extract_text() for page in reader.pages if page.extract_text())

# parsing JSON
def extract_json_block(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            print("error parsing json")
            return None
    return None

# recommend jobs
def get_job_suggestions(resume_text):
    prompt = f"""Read the resume below and suggest 4 technology-related career fields/jobs that match the candidate's experience.
If there are no matching fields, respond with an empty list.
Respond strictly in this JSON format without any additional output:
{{
    "suggested_jobs": [
    {{"job": "Job Name", "description": "What the field/job is all about", "skills_required": ["Skill1", "Skill2", .. up to 6 skills]
    }}
    ]
}}

Resume:
{resume_text}
    """
    res = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [{"role": "user", "content": prompt}]
    )
    raw = res.choices[0].message.content
    parsed = extract_json_block(raw)
    if parsed: 
        return parsed
    else:
        print("error generating jobs")

# make an assessment quiz
def generate_assessment(field, role, skills):
    skill_str = ", ".join(skills)
    prompt = f"""Create a 3-question quiz (no multiple choice and text input answers) to assess a beginner applicant for the role of {role} in the {field} field.

    Base the questions on the following required technical skills: {skill_str}

    Respond strictly in this JSON format without any additional output:
    {{
    "questions: [
        {{
        "question": "Text",
        "answer": "Correct Answer"
        }}
        ] 
    }}
    """
    res = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        return json.loads(res.choices[0].message.content)["questions"]
    except:
        print("could not generate quiz.")
        return []
    
def generate_upskilling_roadmap(skills):
    prompt = f"""Suggest a free learning roadmap for the following skills: {', '.join(skills)}.
    Include a guide and some free learning resources per skill + short description of the skill. Respond strictly in this JSON format:
    {{
    "roadmap": [
        {{
        "skill": "Skill Name",
        "description": "Short description of skill",
        "resources": ["Free resource link"]
        }}
    ]
    }}
    """
    res = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
    )
    try:
        parsed = extract_json_block(res.choices[0].message.content)
        return parsed["roadmap"] if parsed and "roadmap" in parsed else []
    except: 
        print("failed to generate upskilling roadmap.")
        return []

def is_answer_similar(user_answer, correct_answer):
    prompt: f"""You are a grading assistant. Compare the user's answer to the correct answer and return only \"yes\" or \"no\".

    Correct answer: "{correct_answer}"
    User's answer: "{user_answer}"

    Is the user's answer close enough in meaning to be considered correct? Answer only with \"yes\" or \"no\".
"""
    try:
        res = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user", "content": prompt}]
        )
        result = res.choices[0].message.content.strip().lower()
        return "yes" in result
    except:
        return False
