from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.context_processor
def example():
    return dict(myexample='This is an context processor basic example')

@app.context_processor
def example2():
    def isAdmin(user):
        if user == "luke":
            returnValue = 1
        else:
            returnValue = 0
        return returnValue
    return dict(isAdmin=isAdmin)
