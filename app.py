from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(_name_)

# Home page route
@app.route('/')
def home():
    return render_template("templates/index.html")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    nitrogen = float(request.form['nitrogen'])
    phosphorus = float(request.form['phosphorus'])
    potassium = float(request.form['potassium'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph_value = float(request.form['ph_value'])
    rainfall = float(request.form['rainfall'])

    with open("trained_model.pkl", "rb") as file:
       model = pickle.load(file)
   # Prepare input for prediction
    input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]])
    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction_text=f'Predicted Price: ₹{round(prediction, 2)} per quintal')

if _name_ == '_main_':

    app.run(debug=True)



