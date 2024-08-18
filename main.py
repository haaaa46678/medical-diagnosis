from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Initialize Flask application
app = Flask(__name__)

# Load the trained model
model = RandomForestClassifier(random_state=42)
# Assuming you have trained your model before and saved it, then you can load it here
# model = joblib.load('your_model_file.pkl')

# Load the symptoms list
df = pd.read_csv('Training.csv')
symptoms = df.columns[:-1].tolist()

# Define the home route
@app.route('/')
def home():
    return render_template('index.html', symptoms=symptoms)

# Define the prediction route
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Extracting values from form
#     selected_symptoms = {symptom: int(request.form[symptom]) for symptom in symptoms}
    
#     # Prepare data for prediction
#     input_data = pd.DataFrame({symptom: [selected_symptoms[symptom]] for symptom in symptoms})
#     input_encoded = pd.get_dummies(input_data)
#     input_encoded = input_encoded.reindex(columns=model.feature_names_in_, fill_value=0)
    
#     # Make prediction
#     prediction = model.predict(input_encoded)[0]
    
#     return render_template('result.html', prediction=prediction)


# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Extracting values from form
    selected_symptoms = {symptom: int(request.form[symptom]) if request.form[symptom] else 0 for symptom in symptoms}
    
    # Prepare data for prediction
    input_data = pd.DataFrame({symptom: [selected_symptoms[symptom]] for symptom in symptoms})
    input_encoded = pd.get_dummies(input_data)
    input_encoded = input_encoded.reindex(columns=model.feature_names_in_, fill_value=0)
    
    # Make prediction
    prediction = model.predict(input_encoded)[0]
    
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)