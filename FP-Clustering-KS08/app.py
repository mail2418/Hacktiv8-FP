from flask import Flask, render_template, request
import numpy as np
import pickle

# KMeans Model
model = pickle.load(open('model/kmeans.pkl', 'rb'))
# Scaller Model
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

app = Flask(__name__, template_folder="templates")


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)