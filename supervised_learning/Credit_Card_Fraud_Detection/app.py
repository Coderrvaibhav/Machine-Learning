from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
model = pickle.load(open("your_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Extract input data from form
    features = [float(request.form[f"V{i}"]) for i in range(1, 29)]
    features.insert(0, float(request.form["Time"]))  # Add 'Time' feature at index 0
    features.append(float(request.form["Amount"]))  # Add 'Amount' feature at the end

    # Convert to numpy array and reshape
    final_features = np.array(features).reshape(1, -1)

    # Make prediction
    prediction = model.predict(final_features)

    result = "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"

    return render_template("result.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
