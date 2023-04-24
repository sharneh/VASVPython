from flask import Flask, render_template, request
from flask_wtf import CsrfProtect


app = Flask(__name__)

app.secret_key = b'_53rtyujhdjhdhjh'
csrf = CsrfProtect(app)


@app.route("/protectedCSRFForm", methods=['GET', 'POST'])
def protectedcsrf_form():
    if request.method == 'POST':
        name = request.form['uname']
        return 'Great ' + name + '!!!!! You have passed secret key.'
    return render_template('index.html')


@app.route("/unprotectedCSRFForm", methods=['GET', 'POST'])
def unprotectedcsrf_form():
    if request.method == 'POST':
        name = request.form['uname']
        return 'OOPS ' + name + '!!!!! No secret key found.'
    return render_template('indexUnprotected.html')

if __name__ == '__main__':
    app.run(debug=True)

