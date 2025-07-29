from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def gate():
    return render_template("gate.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/travel_guide")
def travel_guide():
    return render_template("travel_guide.html")

@app.route("/rsvp", methods=["POST"])
def rsvp():
    name = request.form.get("name")
    attending = request.form.get("attending")
    return render_template("thank_you.html", name=name, attending=attending)

@app.route("/faq")
def faq():
    return render_template("faq.html")

if __name__ == "__main__":
    app.run(debug=True)
