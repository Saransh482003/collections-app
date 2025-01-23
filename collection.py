from flask import Flask, request

app = Flask(__name__)
#fdsf
@app.route("/")
def index():
    return "Hello, World!"

@app.route("/<month>")
def hello_collection(year):
    generation = ""
    year = int(year)
    if year >2000 and year < 2015:
        generation = "Gen Z"
    elif year >2015:
        generation = "Gen Alpha"
    elif year < 2000:
        generation = "Millennials"
    else:
        generation = "Gen Omega"
    return {
        "year": year,
        "generation": generation}


if __name__ == "__main__":
    app.run()