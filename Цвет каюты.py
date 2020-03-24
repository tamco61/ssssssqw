from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def odd_even(sex, age):
    return render_template('table.html', title='Заготовка', sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')