from flask import Flask, Request, render_template, request
from joblib import load
import pandas as pd
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")
@app.route('/predict/<years>',methods=['GET', 'POST'])
def predict(years):
    # if request.method == 'POST':
        # Charger le modèle sauvegardé
    years=[[years]]
    t=pd.DataFrame(years,columns=["Years of Experience"])
    reg_loaded = load('model.joblib')
    x=reg_loaded.predict(t)
    return f" {int(x[0])} Euro"


if __name__ == '__main__':
    app.run(debug=True)