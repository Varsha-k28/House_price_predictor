from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = np.array([[
        int(data["overall_quality"]),
        float(data["living_area"]),
        int(data["garage_capacity"]),
        float(data["basement_area"]),
        int(data["full_bath"]),
        int(data["year_built"])
    ]])

    prediction = model.predict(features)

    return jsonify({
        "price": round(float(prediction[0]), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)