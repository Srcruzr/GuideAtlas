from flask import Flask, render_template, send_from_directory

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

@app.route("/pociones-ashen-ruins")
def pociones_pociones_ashen_ruins():
    return render_template("pociones-ashen-ruins.html")

@app.route("/cofres-secretos")
def cofres_secretos():
    return render_template("cofres-secretos.html")

@app.route("/cofres-secretos-ashen-ruins")
def cofres_secretos_ashen_ruins():
    return render_template("cofres-secretos-ashen-ruins.html")

@app.route("/materiales-departure-isle")
def materiales_departure_isle():
    return render_template("materiales-departure-isle.html")

@app.route("/materiales-ashen-ruins")
def materiales_ashen_ruins():
    return render_template("materiales-ashen-ruins.html")

@app.route("/enchantments")
def enchantments():
    return render_template("enchantments.html")

@app.route("/event-gear")
def event_gear():
    return render_template("event-gear.html")

@app.route("/materials-spirit")
def materials_spirit():
    return render_template("materials-spirit.html")

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)