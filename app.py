from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.context_processor
def example():
    return dict(myexample='This content made by a context processor')



@app.context_processor
def example2():
    def isLukeFunc(user):
        if user == "luke":
            returnValue = 1
        else:
            returnValue = 0
        return returnValue
    return dict(isLuke=isLukeFunc)
