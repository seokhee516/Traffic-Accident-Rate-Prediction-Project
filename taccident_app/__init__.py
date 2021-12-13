import os
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)
model = pickle.load(open("rf_model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/result', methods=['GET','POST'])
def predict():
    data1 = request.form["월"]
    data2 = request.form["요일"]
    data3 = request.form["발생지_시도"]
    data4 = request.form["기상상태"]
    input_data = pd.DataFrame([[data1, data2, data3, data4]], columns=['월', '요일', '발생지_시도', '기상상태'])
    pred = model.predict(input_data)
    pred = int(np.around(pred))
    
    mean_accident = 620
    rate_of_change = int(np.around(((pred - mean_accident)/mean_accident)*100))
    
    return render_template("result.html", pred=pred, rate_of_change=rate_of_change, \
        month=data1, day_of_the_week=data2, city=data3, weather=data4)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/information')
def infomation():
    return render_template('information.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
    
    
