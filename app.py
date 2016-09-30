from flask import Flask, render_template, request

app = Flask(__name__)

username = "nick"
password = "password"

@app.route("/")
@app.route("/login/")
def templayte():
    print request.headers
    return render_template('newtemp.html')

@app.route('/authenticate/', methods =['POST'])
def auth():
    if request.form['un'] == "nick" and request.form['pw'] == "password":
        return render_template('success.html')
    else:
        return render_template('failure.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
