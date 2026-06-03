from flask import Flask, render_template

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guides-wizard")
def guides_wizard():
    return render_template("guides-wizard.html")

@app.route("/codes-wizard")
def codes_wizard():
    return render_template("codes-wizard.html")

@app.route("/pociones-departure-isle")
def pociones_departure_isle():
    return render_template("pociones-departure-isle.html")

@app.route("/cofres-secretos")
def cofres_secretos():
    return render_template("cofres-secretos.html")

@app.route("/cofres-secretos-ashen-ruins")
def cofres_secretos_ashen_ruins():
    return render_template("cofres-secretos-ashen-ruins.html")

@app.route("/googlee6a931a6b04cb4d2")
def googlee6a931a6b04cb4d2():
    return render_template("googlee6a931a6b04cb4d2.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)