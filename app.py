from flask import Flask, request, render_template

from password_generator_service.utilities import generate_password

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        length = request.form['Length']
        generation = generate_password(length)

        output = generation
        # if output == 0:
        return render_template('home.html',
                               result=output)
        # else:
        #     return render_template('home.html',
        #                            prediction_text="Heart disease possibility is more")

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=7777)
