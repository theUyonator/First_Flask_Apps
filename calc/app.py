# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def opp_add():
    """Add a and b and display the answer in the /add route"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a,b)
    return str(result)

@app.route("/sub")
def opp_sub():
    """Subtract b from a and display the result in the /sub route"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a,b)
    return str(result) 

@app.route("/mult")
def opp_mult():
    """Multiply a by b and display the result in the /mult route"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a,b)
    return str(result) 

@app.route("/div")
def opp_div():
    """Divide a by b and display the result in the /div route"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a,b)
    return str(result) 

"""Now this is a route that can deal with 4 different urls at the same time"""

# First we create a dict to hold our variable urls

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

# Then we make a route to hold a variable url

@app.route("/math/<opp>")
def do_math(opp):
    """This function carries out any of the four operations in the operations dict"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations[opp](a,b)

    return str(result)