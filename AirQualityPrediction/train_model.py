import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Generate sample dataset
data = {
    "Temperature": np.random.randint(20, 40, 100),
    "Humidity": np.random.randint(30, 80, 100),
    "CO2": np.random.randint(300, 1000, 100),
    "Dust": np.random.randint(50, 300, 100),
}
df = pd.DataFrame(data)

# Assume AQI is affected by these factors
df["AQI"] = df["Temperature"] * 1.2 + df["Humidity"] * 0.8 + df["CO2"] * 0.5 + df["Dust"] * 0.3 + np.random.randint(-10, 10, 100)

# Split data
X = df[["Temperature", "Humidity", "CO2", "Dust"]]
y = df["AQI"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")
