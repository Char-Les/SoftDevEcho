# Charles Weng
# SoftDev1 pd 7
# HW06 -- Echo Echo Echo
# 2017-10-3

from flask import Flask, render_template, request
import random

app = Flask(__name__)

# landing page
@app.route("/")
def root():
    return render_template("root.html")

# Page that has the goods
@app.route("/echo")
def echo():
    debug()
    form = request.args
    return render_template("echo.html", name = form['user'], meth = request.method)

# michael's debug statements from lct
def debug():
    print "\n\n\n"
    print "app:"
    print app
    print "\nrequest.headers:"
    print request.headers
    print "\nrequest.method:"
    print request.method
    print "\nrequest.args:"
    print request.args

if __name__ == "__main__":
    app.debug = True
    app.run()
