from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/events")
def events():
    return "Events"

@app.route("/metrics")
def metrics():
    return "Metrics"

@app.route("/auth/login")
def auth_login():
    return "Auth_Login"

if __name__ == '__main__':
    app.run()
