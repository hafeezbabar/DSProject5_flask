from flask import Flask, request, render_template, Request

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/Gallery")
def gallery():
    return "<h1>Gallery</h>"

@app.route("/form", methods=['post','get'])
def form():

    if request.method == 'GET':
        return render_template('form.html')
    else:
        math=float(request.form['math'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average = (math+science+history)/3

    return render_template("home.html", score=average)

if __name__=="__main__":
    app.run(debug=True)

