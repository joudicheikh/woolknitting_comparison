from flask import Flask, render_template, request, redirect, url_for
from search import searchWollplatz
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def first_page():
    if request.method == "POST":
        if request.form["first_query"] and request.form["first_query"]:
            result1 = request.form["first_query"]
            result2 = request.form["second_query"]
            products = []
            product_wollplatz = searchWollplatz(str(result1), str(result2))
            products.append(product_wollplatz)
            return render_template("results.html", products=products, brand=result1, product_name=result2)
    else:
        return render_template("welcome.html")


if __name__ == '__main__':
    app.run()