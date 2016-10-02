from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

username = "nick"
password = "password"



@app.route("/")
def templayte():
    return render_template('newtemp.html')

@app.route('/authenticate/', methods =['POST'])
def auth():
    m=hashlib.md5()
    if request.form['un'] != '' and request.form['pw']!='':
        if request.form['input'] == 'Create Account':
            pen = open("data/usernames.csv",'r')
            pineapple = pen.readlines()
            pen.close()
            for item in pineapple:
                if request.form['un'] == item.split(',')[0]:
                    return render_template('newtemp.html',floo='That account name already exists!')
            #print 'hi'
            apple = open("data/usernames.csv",'a')
            m.update(request.form['pw'])
            apple.write(request.form['un']+','+m.hexdigest()+'\n')
            apple.close()
            return render_template('newtemp.html',floo='Account Created!')
        else:
            pen = open('data/usernames.csv','r')
            applepen = pen.readlines()
            pen.close()
            for line in applepen:
                un = request.form['un']
                c = hashlib.md5()
                c.update(request.form['pw'])
                pw = c.hexdigest()
                if un == line.split(',')[0]:
                    if pw == line.split(',')[1].strip():
                        return render_template('success.html')
                    return render_template('newtemp.html', floo = 'Incorrect password')
            return render_template('newtemp.html',floo='Account not found')
    else:
        return render_template('newtemp.html')




if __name__ == "__main__":
    app.debug = True
    app.run()
