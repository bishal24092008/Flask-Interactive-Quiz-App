from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "bishal_op_quiz"

# 10 QUESTIONS
questions = [
    {"q": "2 + 2 = ?", "options": ["2","4","6","8"], "a": "4"},
    {"q": "Capital of India?", "options": ["Mumbai","Delhi","Chennai","Goa"], "a": "Delhi"},
    {"q": "Python is?", "options": ["Snake","Programming Language","Bike","Movie"], "a": "Programming Language"},
    {"q": "Sun rises from?", "options": ["West","North","East","South"], "a": "East"},
    {"q": "5 + 7 = ?", "options": ["10","11","12","13"], "a": "12"},
    {"q": "Largest planet?", "options": ["Earth","Mars","Jupiter","Venus"], "a": "Jupiter"},
    {"q": "HTML stands for?", "options": ["Hyper Text Markup Language","High Text Machine Language","Hyper Tool Multi Language","None"], "a": "Hyper Text Markup Language"},
    {"q": "CPU is?", "options": ["Brain of Computer","Input Device","Output Device","Storage"], "a": "Brain of Computer"},
    {"q": "RAM stands for?", "options": ["Random Access Memory","Read Active Memory","Rapid Act Memory","None"], "a": "Random Access Memory"},
    {"q": "9 × 9 = ?", "options": ["72","81","79","99"], "a": "81"},
]


@app.route("/")
def start():
    session["score"] = 0
    session["index"] = 0

    q_copy = questions.copy()
    random.shuffle(q_copy)
    session["quiz"] = q_copy[:10]

    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    index = session.get("index", 0)
    quiz = session.get("quiz")

    if request.method == "POST":
        selected = request.form.get("option")

        if selected == quiz[index]["a"]:
            session["score"] += 1

        session["index"] += 1
        index = session["index"]

        if index >= len(quiz):
            return redirect(url_for("result"))

    return render_template(
        "index.html",
        question=quiz[index],
        index=index + 1,
        total=len(quiz)
    )


@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(session.get("quiz", []))

    if score <= 4:
        msg = "😢 Try Again!"
    elif score <= 7:
        msg = "🙂 Good!"
    else:
        msg = "🎉 Excellent!"

    return render_template(
        "result.html",
        score=score,
        total=total,
        msg=msg
    )


if __name__ == "__main__":
    app.run(debug=True)
