

# Disease Predictor

This is a web application for predicting diseases based on symptoms using a machine learning model.

## Introduction
This project aims to provide a simple and user-friendly interface for predicting diseases based on symptoms input by the user. It utilizes a Random Forest Classifier model trained on a dataset containing symptoms and corresponding disease diagnoses.

## Features
- Users can input their symptoms through a web form.
- The model predicts the most probable disease based on the provided symptoms.
- The application provides accuracy metrics for both training and testing data.
- Users can interactively explore the model's predictions for different symptom combinations.

## Requirements
- Python 3.x
- Flask
- scikit-learn
- pandas
- ipywidgets (for interactive symptom selection)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Vikhyathsai11/diagnosis.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```
   python app.py
   ```
2. Access the application in your web browser at `http://localhost:5000`.

## File Structure
- `app.py`: Main Flask application file.
- `templates/`: HTML templates for the web application.
- `static/`: Static files (CSS, JavaScript).
- `data/`: Dataset files (`Training.csv`, `Testing.csv`).
- `model/`: Trained machine learning model (`random_forest_model.pkl`).
- `README.md`: This file.

![Screenshot 2024-02-26 212840](https://github.com/Vikhyathsai11/diagnosis/assets/115020382/0db39d85-2aed-4c1c-a0d1-3a6bd7a9ff8f)

## After Prediction

![Screenshot 2024-02-26 213138](https://github.com/Vikhyathsai11/diagnosis/assets/115020382/2f84d79f-73bc-42e9-a3fc-055f6dd32f3a)
