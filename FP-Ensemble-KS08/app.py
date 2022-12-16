from flask import Flask, render_template, request
import numpy as np
import pickle

# KMeans Model
model = pickle.load(open('model/model_ETC_KS08.pkl', 'rb'))

app = Flask(__name__, template_folder="templates")

@app.route("/predict", methods=['POST'])
def predict():
    age = float(request.form["age"])
    anaemia = float(request.form["anaemia"])
    creatinine_phosphokinase = float(request.form["creatinine_phosphokinase"])
    diabetes = float(request.form["diabetes"])
    high_blood_pressure = float(request.form["high_blood_pressure"])
    platelets = float(request.form["platelets"])
    serum_creatinine = float(request.form["serum_creatinine"])
    sex = float(request.form["sex"])
    smoking = float(request.form["smoking"])
    young_person = float(request.form["young_person"])

    float_feature = [
        age,
        anaemia,
        creatinine_phosphokinase,
        diabetes,
        high_blood_pressure,
        platelets,
        serum_creatinine,
        sex,
        smoking,
        young_person
    ]

    final_feature = [np.array(float_feature)]
    prediction = model.predict(final_feature)

    output={0:'Pasien cenderung Hidup',
            1:'Pasien cenderung Meninggal'}
    
    return render_template('index.html', prediction_text = 'Berdasarkan nilai dari inputan, maka {} '.format(output[prediction[0]]))
    # return render_template('index.html', prediction_text = 'Fitur {}'.format(prediction[0]))


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)