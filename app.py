from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Devops project 1 is running"

@app.route("/health")
def health():
    return {"Status":"Healthy"}

@app.route("/time")
def time():
    return { 
            "current_time":
            str(datetime.datetime.now())
            }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

