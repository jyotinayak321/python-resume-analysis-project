from flask import Flask, render_template, request
import PyPDF2
from resume_checker import check_resume

app = Flask(__name__)

def extract_text_from_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

@app.route("/", methods=["GET", "POST"])
def home():

    skills = []
    score = None
    result = None

    if request.method == "POST":

        pdf_file = request.files["resume"]

        if pdf_file:
            resume_text = extract_text_from_pdf(pdf_file)

            skills, score, result = check_resume(resume_text)

    return render_template("index.html",
                           skills=skills,
                           score=score,
                           result=result)

if __name__ == "__main__":
    app.run(debug=True)