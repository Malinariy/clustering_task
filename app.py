import numpy as np
import flask
import pickle
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('main.html')


def ValuePredictor(to_predict_list):

    to_predict = np.array(to_predict_list).reshape(1,2)
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    result = loaded_model.predict(to_predict) #предсказываю значение используя загруженную модель
    return result[0]


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.values()
        print('to_predict_list0:', to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print('to_predict_list1:', to_predict_list)
        results = ValuePredictor(to_predict_list)

        if float(results) == 1:
            my_prediction = 'Клиент с высоким годовым доходом и очень низкой убыточностью'
        elif float(results) == 0:
            my_prediction = 'Клиент со средним годовым доходом, средним или высоким показателем убыточности'

        return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=False)
