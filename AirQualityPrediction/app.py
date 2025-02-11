from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained regression model (For now, we use a dummy function)
def predict_aqi(features):
    # Example Regression Formula (Replace with your model)
    aqi = (features[0] * 1.5) + (features[1] * 2.2) + (features[2] * 0.8) + (features[3] * 3.0)
    return round(aqi, 1)

# Function to classify air quality based on AQI
def get_air_quality_label(aqi):
    if aqi <= 100:
        return "Good", "good"
    elif aqi <= 150:
        return "Moderate", "moderate"
    else:
        return "Unhealthy", "unhealthy"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        co2 = float(request.form["co2"])
        dust = float(request.form["dust"])

        # Make prediction
        features = np.array([temperature, humidity, co2, dust])
        predicted_aqi = predict_aqi(features)

        # Get label and CSS class
        label, label_class = get_air_quality_label(predicted_aqi)

        return render_template("index.html", prediction=predicted_aqi, label=label, label_class=label_class)

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
