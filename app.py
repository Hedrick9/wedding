from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/rsvp", methods=["POST"])
def rsvp():
    name = request.form.get("name")
    attending = request.form.get("attending")
    return render_template("thank_you.html", name=name, attending=attending)

if __name__ == "__main__":
    app.run(debug=True)
