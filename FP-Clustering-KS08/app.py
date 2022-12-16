from flask import Flask, render_template, request
import numpy as np
import pickle

# KMeans Model
model = pickle.load(open('model/kmeans.pkl', 'rb'))
# Scaller Model
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

app = Flask(__name__, template_folder="templates")

@app.route("/predict", methods=['POST'])
def predict():
    BALANCE = float(request.form["BALANCE"])
    BALANCE_FREQUENCY = float(request.form["BALANCE_FREQUENCY"])
    PURCHASES = float(request.form["PURCHASES"])
    ONEOFF_PURCHASES = float(request.form["ONEOFF_PURCHASES"])
    INSTALLMENTS_PURCHASES = float(request.form["INSTALLMENTS_PURCHASES"])
    CASH_ADVANCE = float(request.form["CASH_ADVANCE"])
    PURCHASES_FREQUENCY = float(request.form["PURCHASES_FREQUENCY"])
    ONEOFF_PURCHASES_FREQUENCY = float(
        request.form["ONEOFF_PURCHASES_FREQUENCY"])
    PURCHASES_INSTALLMENTS_FREQUENCY = float(
        request.form["PURCHASES_INSTALLMENTS_FREQUENCY"])
    CASH_ADVANCE_FREQUENCY = float(request.form["CASH_ADVANCE_FREQUENCY"])
    CASH_ADVANCE_TRX = float(request.form["CASH_ADVANCE_TRX"])
    PURCHASES_TRX = float(request.form["PURCHASES_TRX"])
    CREDIT_LIMIT = float(request.form["CREDIT_LIMIT"])
    PAYMENTS = float(request.form["PAYMENTS"])
    MINIMUM_PAYMENTS = float(request.form["MINIMUM_PAYMENTS"])
    PRC_FULL_PAYMENT = float(request.form["PRC_FULL_PAYMENT"])
    TENURE = float(request.form["TENURE"])

    feature = [
        BALANCE,
        BALANCE_FREQUENCY,
        PURCHASES,
        ONEOFF_PURCHASES,
        INSTALLMENTS_PURCHASES,
        CASH_ADVANCE,
        PURCHASES_FREQUENCY,
        ONEOFF_PURCHASES_FREQUENCY,
        PURCHASES_INSTALLMENTS_FREQUENCY,
        CASH_ADVANCE_FREQUENCY,
        CASH_ADVANCE_TRX,
        PURCHASES_TRX,
        CREDIT_LIMIT,
        PAYMENTS,
        MINIMUM_PAYMENTS,
        PRC_FULL_PAYMENT,
        TENURE
    ]

    final_feature = [np.array(feature)]
    scaled_feature = scaler.fit_transform(final_feature)
    prediction = model.predict(scaled_feature)

    output={0:'Orang yang tidak hedon',
            1:'Orang yang sedikit hedon',
            2:'Orang yang terlalu hedon'}
    
    return render_template('index.html', prediction_text = 'Berdasarkan nilai dari inputtan, maka orang tersebut berada pada cluster {} yang mana merupakan {}'.format(prediction[0], output[prediction[0]]))
    # return render_template('index.html', prediction_text = 'Fitur {}'.format(prediction[0]))


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)