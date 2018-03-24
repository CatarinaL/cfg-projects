from flask import Flask, render_template, request

app = Flask("FlaskApp")

@app.route("/") # decorator
def say_hello():
    #return "Hello Flask!"
    return render_template("index.html")

app.run(debug = True) # debug is iseful for development
                    #but shouldn't be used in production
