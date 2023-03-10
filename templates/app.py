#from django.db import router
#from crypt import methods
import joblib
from flask import Flask, render_template, request
import preprocess 

app = Flask(__name__, template_folder="../templates")

model = joblib.load(r'Models\last_model.h5')


@app.route('/')
def index() :
    return render_template('index.html') 

@app.route("/predict", methods=["POST"])
def get_prediction():
    if request.method == "POST":
        home_team = request.form["home_team"]
        away_team = request.form["away_team"]

    data = {"home_team" : home_team, "away_team" : away_team}

    final_data = preprocess.preprocess_data(data)
    
    
    def home_team_result(result):
        if result == 2:
            return "Win"
        elif result == 1:
            return "Draw"
        else:
            return "Lose" 

    prediction = f"{home_team} Will {home_team_result(model.predict([final_data]))}"
    return render_template("prediction.html", match_result_prediction=prediction)


if __name__ == '__main__' :
    app.run(debug=True)