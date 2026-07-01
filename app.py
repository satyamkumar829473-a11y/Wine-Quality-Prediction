from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("wine_quality_model.pkl", "rb"))
data = pd.read_csv("winequality.csv")

# Remove Id column if present
if "Id" in data.columns:
    data = data.drop("Id", axis=1)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["fixed_acidity"]),
        float(request.form["volatile_acidity"]),
        float(request.form["citric_acid"]),
        float(request.form["residual_sugar"]),
        float(request.form["chlorides"]),
        float(request.form["free_sulfur_dioxide"]),
        float(request.form["total_sulfur_dioxide"]),
        float(request.form["density"]),
        float(request.form["ph"]),
        float(request.form["sulphates"]),
        float(request.form["alcohol"])
    ]

    # Check whether the exact values exist in the CSV
    match = data[
        (data["fixed acidity"] == features[0]) &
        (data["volatile acidity"] == features[1]) &
        (data["citric acid"] == features[2]) &
        (data["residual sugar"] == features[3]) &
        (data["chlorides"] == features[4]) &
        (data["free sulfur dioxide"] == features[5]) &
        (data["total sulfur dioxide"] == features[6]) &
        (data["density"] == features[7]) &
        (data["pH"] == features[8]) &
        (data["sulphates"] == features[9]) &
        (data["alcohol"] == features[10])
    ]

    if match.empty:
        return render_template(
            "index.html",
            error="❌ Error: Entered values do not match any record in the dataset."
        )

    prediction = model.predict([features])[0]

    return render_template(
        "index.html",
        prediction=f"Predicted Wine Quality: {prediction:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)