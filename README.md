# 🩺 Liver Disease Prediction Web App

A Machine Learning–powered web application that predicts the likelihood of **liver disease** based on patient-provided clinical and demographic features.

The project uses **Python, Scikit-learn, Flask, HTML, and CSS** to build a complete end-to-end machine learning application — from data preprocessing and model training to web-based prediction.

> **⚠️ Medical Disclaimer:** This application is intended for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used as a substitute for professional medical evaluation or clinical diagnosis.

---

## 📌 Project Overview

Liver disease can be associated with various clinical indicators such as bilirubin levels, liver enzymes, age, and other patient characteristics.

This project demonstrates how machine learning can be used to learn patterns from a liver disease dataset and provide a prediction through a simple web interface.

### Workflow

```text
Patient Input
     ↓
Flask Web Interface
     ↓
Data Preprocessing
     ↓
Trained ML Model
     ↓
Prediction
     ↓
Result Display
```

---

## ✨ Features

* 🧠 Machine Learning–based liver disease prediction
* 🌐 Flask-based web application
* 🎨 Responsive HTML/CSS interface
* 📊 Data preprocessing and feature scaling
* 💾 Saved trained model using Pickle
* 💾 Saved fitted `StandardScaler`
* ⚡ Real-time prediction through the web interface
* 📱 User-friendly medical-style interface
* 🔄 Complete ML workflow from training to deployment

---

## 🛠️ Technologies Used

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Core programming language          |
| Pandas       | Data loading and preprocessing     |
| NumPy        | Numerical operations               |
| Scikit-learn | Machine Learning and preprocessing |
| Flask        | Web application backend            |
| HTML         | Frontend structure                 |
| CSS          | UI styling                         |
| Pickle       | Model serialization                |

---

## 📂 Project Structure

```text
liver_disease_app/
│
├── static/
│   └── style.css
│       # Custom medical-style CSS
│
├── templates/
│   └── index.html
│       # Responsive web interface
│
├── liver_disease.csv
│   # Liver disease dataset
│
├── model.pkl
│   # Trained Machine Learning model
│
├── scaler.pkl
│   # Fitted StandardScaler object
│
├── train_and_save.py
│   # Data preprocessing, model training
│   # and model serialization
│
└── app.py
    # Flask backend application
```

---

## 🔬 Machine Learning Workflow

The project follows a standard machine learning pipeline:

### 1. Data Loading

The liver disease dataset is loaded using Pandas.

```python
import pandas as pd

df = pd.read_csv("liver_disease.csv")
```

### 2. Data Preprocessing

The dataset is prepared for machine learning by handling the required preprocessing steps, such as:

* Feature selection
* Missing-value handling
* Categorical data processing
* Numerical feature preparation
* Feature scaling

### 3. Feature Scaling

Numerical features are scaled using `StandardScaler`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

The fitted scaler is saved so that the **same transformation** can be applied when new patient data is entered into the application.

### 4. Model Training

A classification model is trained using the prepared dataset.

The trained model is then serialized using Pickle:

```python
import pickle

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
```

### 5. Prediction

When a user enters patient information through the web interface:

```text
User Input
    ↓
Preprocessing / Scaling
    ↓
Trained Model
    ↓
Prediction
    ↓
Result
```

---

## 📊 Dataset

The project uses a liver disease dataset containing clinical and demographic information about patients.

Example features may include:

* Age
* Gender
* Total Bilirubin (TB)
* Direct Bilirubin (DB)
* Alkaline Phosphatase (ALP)
* Alanine Aminotransferase (ALT)
* Aspartate Aminotransferase (AST)
* Total Proteins
* Albumin
* Albumin and Globulin Ratio

The target variable represents the liver disease classification.

> Dataset characteristics and feature names depend on the specific dataset used for training.

---

## 🧠 Model Components

The project separates the trained model and preprocessing object:

### `model.pkl`

Contains the trained machine learning classifier.

### `scaler.pkl`

Contains the fitted `StandardScaler`.

Keeping the scaler from training is important because the same scaling parameters must be used during prediction.

```text
Training Data
     ↓
Fit Scaler
     ↓
Transform Data
     ↓
Train Model
     ↓
Save Model + Scaler
```

During prediction:

```text
New Patient Data
     ↓
Load Saved Scaler
     ↓
Transform Input
     ↓
Load Saved Model
     ↓
Prediction
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/liver_disease_app.git
```

Move into the project directory:

```bash
cd liver_disease_app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required libraries:

```bash
pip install flask pandas numpy scikit-learn
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

You should see a local address similar to:

```text
http://127.0.0.1:5000/
```

Open this address in your browser to use the application.

---

## 🔄 Retraining the Model

If you want to train the model again using the dataset, run:

```bash
python train_and_save.py
```

This script handles the model-training workflow and generates the required serialized files.

After training, start the Flask application:

```bash
python app.py
```

---

## 🖥️ Application Interface

The application provides a simple web interface where users can enter the required patient information.

```text
┌─────────────────────────────────────┐
│       Liver Disease Prediction      │
├─────────────────────────────────────┤
│                                     │
│  Age:             [        ]        │
│  Gender:          [        ]        │
│  Total Bilirubin: [        ]        │
│  Direct Bilirubin:[        ]        │
│  ALT:             [        ]        │
│  AST:             [        ]        │
│                                     │
│        [ Predict ]                  │
│                                     │
│  Prediction Result                  │
│                                     │
└─────────────────────────────────────┘
```

---

## 📁 Important Files

### `app.py`

The Flask backend responsible for:

* Loading the trained model
* Loading the scaler
* Receiving user input
* Preprocessing input
* Generating predictions
* Returning the prediction result to the frontend

### `train_and_save.py`

Responsible for:

* Loading the dataset
* Preparing the data
* Training the model
* Fitting the scaler
* Saving the trained objects

### `templates/index.html`

Contains the frontend structure and prediction form.

### `static/style.css`

Contains the custom styling for the application.

### `model.pkl`

Serialized trained model.

### `scaler.pkl`

Serialized fitted scaler.

---

## 📌 Key Learning Outcomes

Through this project, the following concepts are demonstrated:

* Data preprocessing
* Feature selection
* Feature scaling
* Supervised Machine Learning
* Classification
* Model training
* Model serialization
* Flask deployment
* Connecting ML models with web applications
* Building an end-to-end ML project

---

## 🔮 Future Improvements

Possible improvements include:

* Add multiple model comparison
* Display prediction probability
* Add model evaluation metrics
* Add confusion matrix and classification report
* Improve frontend design
* Add input validation
* Add prediction history
* Deploy the application online
* Add a complete preprocessing pipeline
* Add automated testing

---

## ⚠️ Medical Disclaimer

This project is developed for **educational and machine learning demonstration purposes**.

The predictions generated by this application should **not be considered medical advice, diagnosis, or treatment recommendations**. Real-world medical decisions should be made by qualified healthcare professionals using appropriate clinical evaluation and testing.

---

## 👨‍💻 Author
Hamid

Machine Learning / AI Project
