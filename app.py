from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("Environment","development")
    return {
            "message":"Devops project 1 is running",
            "environment":environment
            }

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

