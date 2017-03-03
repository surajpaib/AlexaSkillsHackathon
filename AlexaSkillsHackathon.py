from flask import Flask
from flask_ask import Ask, question, statement, session
import time

app = Flask(__name__)
ask = Ask(app, "/myfirstalexaapp")

@app.route('/')
def home():
    return 'Hello World!'

@ask.launch
def start_skill():
    return question("Hello, How can I help?")

@ask.intent("Time")
def share_time():
    current = time.localtime()
    current_time = {
        'date-day' : current[2],
        'date-month' : current[1],
        'date-year' : current[0],
        'time' : "The current time is {0} hours and {1} minutes".format(current[3], current[4])
    }
    return statement(current_time['time'])


if __name__ == '__main__':
    app.run(debug=True)
