import flask
import numpy as np
import pickle 
from sklearn.preprocessing import StandardScaler

app = flask.Flask(__name__, template_folder="templates")

model = pickle.load(open('model/model_classifier.pkl','rb'))

scaler = StandardScaler()

@app.route('/')
def index():
    return(flask.render_template('index.html'))

@app.route('/predict', methods=['POST'])
def predict():
    #  <!-- ['WindGustSpeed', 'Humidity9am', 'Humidity3pm', 'Cloud9am', 'Cloud3pm','RainToday']  --> 
    
    WindGustSpeed = float(flask.request.form["WindGustSpeed"])
    Humidity9am = float(flask.request.form["Humidity9am"])
    Humidity3pm = float(flask.request.form["Humidity3pm"])
    Cloud9am = float(flask.request.form["Cloud9am"])
    Cloud3pm = float(flask.request.form["Cloud3pm"])
    RainToday = float(flask.request.form["RainToday"])

    data_list = [
        WindGustSpeed,
        Humidity9am,
        Humidity3pm,
        Cloud9am,
        Cloud3pm,
        RainToday
    ]

    final_feature = [np.array(data_list)]
    pred_scaller = scaler.fit_transform(final_feature)
    prediction = model.predict(pred_scaller)
    output = {0: 'Tidak Hujan', 1: 'Hujan'}

    return flask.render_template('index.html', prediction_text = 'Prediksi cuaca besok di Australia adalah {}'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run(debug=True)