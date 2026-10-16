from flask import Flask, render_template, request

app = Flask(__name__)

CAREERS = {
    "web development": {
        "skills": ["HTML", "CSS", "JavaScript", "Python"],
        "description": "Build websites and interactive web applications."
    },
    "data science": {
        "skills": ["Python", "SQL", "Statistics", "Data Analysis"],
        "description": "Analyze data and discover useful patterns."
    },
    "cybersecurity": {
        "skills": ["Networking", "Linux", "Python", "Security"],
        "description": "Help protect systems, networks, and information."
    },
    "ai and machine learning": {
        "skills": ["Python", "Mathematics", "Machine Learning", "SQL"],
        "description": "Develop intelligent systems using data and algorithms."
    },
    "app development": {
        "skills": ["Java", "Kotlin", "Flutter", "APIs"],
        "description": "Create applications for mobile devices."
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    interest = request.form.get("interest", "").strip().lower()
    skills_input = request.form.get("skills", "")
    education = request.form.get("education", "")

    user_skills = {
        skill.strip().lower()
        for skill in skills_input.split(",")
        if skill.strip()
    }

    if interest not in CAREERS:
        return render_template(
            "result.html",
            error="Please select a valid career interest."
        )

    career = CAREERS[interest]
    required_skills = career["skills"]

    matched = [
        skill for skill in required_skills
        if skill.lower() in user_skills
    ]
    missing = [
        skill for skill in required_skills
        if skill.lower() not in user_skills
    ]

    score = round(len(matched) / len(required_skills) * 100)

    return render_template(
        "result.html",
        career_name=interest.title(),
        description=career["description"],
        matched=matched,
        missing=missing,
        score=score,
        education=education,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True)