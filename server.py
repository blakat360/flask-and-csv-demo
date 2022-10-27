from flask import Flask, redirect, url_for, request
import pandas as pd

app = Flask(__name__)

def make_option(val):
    return f"<option value=\"{val}\">{val}</option>"

def create_home(hobby = None):
    with open("./src/index.html", "r") as f:
        s = f.read().replace("lovely", "terrible")
    df = pd.read_csv("./data/hobbies.csv")
    s = s.format("\n".join([make_option(col) for col in df["skill"]]))
    if hobby:
        df = df[df["skill"] == hobby]
    return s + df.to_html(index=False, border = 0)

@app.route("/", methods = ['GET'])
def home():
    return create_home()
    
@app.route("/", methods = ['POST'])
def filtered_home():
    hobby = request.form["interesting_hobbies"]
    print(hobby)
    return create_home(hobby)

@app.route("/programmer_stories")
def programmer_stories():
    with open("./src/programmer_stories.html", "r") as f:
        return f.read()
