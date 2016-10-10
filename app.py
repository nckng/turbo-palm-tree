from flask import Flask, render_template, request, url_for,session,redirect
import hashlib


app = Flask(__name__)
app.secret_key = '\x9f&\xe4\x08\xab\xf6\xafW\xb7}\xa6X\xdcSJk\xf91k& \xa5\xb47\xf1"\x1bE\xab\x026]'
#app.secret_key = 'TSMtsmTSMtsm'


@app.route("/",methods=['GET','POST'])
def templayte():
    if 'user' in session.keys():
        return render_template('landing.html',doo = session['user'])
    else:
        return redirect(url_for('auth'))

@app.route('/logout/',methods = ['POST'])
def logout():
    if 'user' in session.keys():
        session.pop('user')
        return render_template('newtemp.html',floo="You've been logged out")
    else:
        return render_template('newtemp.html',floo="You need to log in first!")
    
@app.route('/authenticate/', methods =['POST','GET'])
def auth():
    m=hashlib.md5()
    if request.method == 'GET':
        return render_template('newtemp.html')
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
                        session['user'] = request.form['un']
                        return render_template('success.html', woo = request.form['un'])
                    return render_template('newtemp.html', floo = 'Incorrect password')
            return render_template('newtemp.html',floo='Account not found')
    else:
        return render_template('newtemp.html')




if __name__ == "__main__":
    app.debug = True
    app.run()
