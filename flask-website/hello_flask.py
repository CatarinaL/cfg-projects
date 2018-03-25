from flask import Flask, render_template, request, send_file
import requests
import numpy as np
import matplotlib as mpl
mpl.use('SVG')
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from io import StringIO
import io
import base64

app = Flask(__name__)

@app.route("/") # decorator
def say_hello():
    #return "Hello Flask!"
    return render_template("hello.html")

@app.route("/<name>")
def say_hello_name(name):
    #return "Hello Flask!"
    return render_template("hello.html", name = name.title())
    #name=name.title() is not necessary, it's only
    #passing name into that variable and applying a method

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    send_to = form_data["email"]
    subject = form_data["subject"]
    message = form_data["content"]
    send_simple_message(send_to, subject, message)
    return "Success, thank you!" #could return render a page, for instance

def send_simple_message(send_to, subject, message):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox86d653487016499fa27f54dcc0e2797c.mailgun.org/messages",
        auth=("api", "key-fb07d651b373f229d0f23615a0380691"),
        #data takes a dictionary
        data={"from": "Catarina :) <postmaster@sandbox86d653487016499fa27f54dcc0e2797c.mailgun.org>",
              "to": send_to,
              "subject": subject,
              "text": message})

@app.route('/image/<param>')
def images(param):
    return render_template("image.html", title = param)

#http://localhost:5000/fig/flip%3D1

@app.route('/fig/<param>')
def fig(param):
    print(param)
    fig = sinplot(flip=param)
    img = BytesIO()
    #fig.savefig(img)
    sns.set()
    plt.savefig(img)
    img.seek(0)
    return img.getvalue()

def return64file(imgvalue):
        #import pdb; pdb.set_trace()
        figdata_png = base64.b64encode(fig(param))
        result = figdata_png
        return send_file(result, attachment_filename='fig.png', mimetype='image/png')

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * float(flip))


app.run(debug = True) # debug is iseful for development
                    #but shouldn't be used in production
