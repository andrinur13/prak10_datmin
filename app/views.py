from os import name
from app import app
from flask import render_template, request

@app.route('/biodata')
def index():
    return render_template('index.html', name="Index")

@app.route('/perhitungan')
def hello():
    return render_template('perhitungan.html', name="Perhitungan")

@app.route('/result', methods=['POST'])
def result():
    tinggi = request.form['tinggi']
    tinggi = int(tinggi)

    alas = request.form['alas']
    alas = int(alas)

    luas = 1/2 * alas * tinggi
    luas = int(luas)

    return render_template('result.html', result=luas)