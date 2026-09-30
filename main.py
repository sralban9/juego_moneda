from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/monedas")
def monedas():
    return render_template("monedas.html")

@app.route("/billetes")
def billetes():
    return render_template("billetes.html")

@app.route("/contar")
def contar():
    return render_template("contar.html")

@app.route("/restar")
def restar():
    return render_template("restar.html")

@app.route("/comprar")
def comprar():
    return render_template("comprar.html")

@app.route("/cambio")
def cambio():
    return render_template("cambio.html")

@app.route("/ahorrar")
def ahorrar():
    return render_template("ahorrar.html")
@app.route("/necesidad")
def necesidad():
    return render_template("necesidad.html")
@app.route("/juego")
def juego():
    return render_template("juego.html")

if __name__ == "__main__":
    app.run(debug=True)