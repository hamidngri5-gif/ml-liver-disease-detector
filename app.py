from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        
        age = float(request.form["age"])
        gender = int(request.form["gender"])
        total_bilirubin = float(request.form["total_bilirubin"])
        direct_bilirubin = float(request.form["direct_bilirubin"])
        alkphos = float(request.form["alkphos"])
        sgpt = float(request.form["sgpt"])
        sgot = float(request.form["sgot"])
        total_proteins = float(request.form["total_proteins"])
        alb = float(request.form["alb"])
        ag_ratio = float(request.form["ag_ratio"])

        
        continuous_features = np.array([[
            age, total_bilirubin, direct_bilirubin, 
            alkphos, sgpt, sgot, 
            total_proteins, alb, ag_ratio
        ]])

        
        scaled_features = scaler.transform(continuous_features)

        
        final_input = np.array([[
            scaled_features[0][0], 
            gender,                
            scaled_features[0][1], 
            scaled_features[0][2], 
            scaled_features[0][3], 
            scaled_features[0][4], 
            scaled_features[0][5], 
            scaled_features[0][6], 
            scaled_features[0][7], 
            scaled_features[0][8]  
        ]])
        # Model Prediction
        prediction = model.predict(final_input)[0]

        if prediction == 1:
            result = "Liver Disease Detected"
            status_class = "danger"
            description = "The patient is at high risk. Further clinical evaluation is recommended."
        else:
            result = "No Liver Disease Detected"
            status_class = "success"
            description = "The patient's metrics are within the normal range."

        return render_template(
            "index.html", 
            prediction_text=result, 
            status_class=status_class,
            description=description
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error in Input: {str(e)}", status_class="danger")

if __name__ == "__main__":
    app.run(debug=True)