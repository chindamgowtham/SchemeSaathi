
from flask import Flask, render_template, request
from eligibility import find_eligible_schemes

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/find-schemes", methods=["POST"])
def find_schemes():

    try:
        user = {
            "name": request.form["name"].strip(),
            "age": int(request.form["age"]),
            "income": float(request.form["income"]),
            "state": request.form["state"],
            "occupation": request.form["occupation"]
        }

        if not user["name"]:
            return "Please enter your name.", 400

        if not 1 <= user["age"] <= 120:
            return "Please enter a valid age.", 400

        if user["income"] < 0:
            return "Income cannot be negative.", 400

        schemes = find_eligible_schemes(user)

        return render_template(
            "results.html",
            user=user,
            schemes=schemes
        )

    except (ValueError, KeyError):
        return "Invalid input. Please check your details.", 400


if __name__ == "__main__":
    app.run(debug=True)

