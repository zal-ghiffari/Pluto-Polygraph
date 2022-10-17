from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from flask_mysqldb import MySQL, MySQLdb
import bcrypt 
import werkzeug
import pandas as pd
from keras.models import load_model
from datetime import datetime

app = Flask(__name__)
app.secret_key = "S3cr3t0VickingLovelySt4aar1!"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pluto_polygraph'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

model_path = 'bilstm1_new61acc.h5'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'id' in session:
        if request.method == 'POST':
            df = pd.read_csv(request.files.get('file'))
            df = df.drop(labels=[' signalLevel', ' blinkStrength', 'timediff'], axis=1)
            df = df[df.loc[:]!=0].dropna()
            df = df.reset_index()
            df = df.drop(labels=['index'], axis=1)
            df = df.astype({" attention": int, " meditation": int, " lowGamma": int, " highGamma": int, " highAlpha": int, " delta": int, " highBeta": int, " lowAlpha": int, " lowBeta": int, " theta": int})
            long_seq = df.shape[0]
            range_diff = 21 - long_seq
            if(long_seq < 21):
                for i in range(range_diff):
                    new_row = {' attention':0, ' meditation':0, ' lowGamma':0, ' highGamma':0,' highAlpha':0, ' delta':0, ' highBeta':0, ' lowAlpha':0, ' lowBeta':0, ' theta':0}
                    df = df.append(new_row, ignore_index=True)
                df = df.iloc[:21]
            else:
                df = df.iloc[:21]
            #avg
            att_avg = df[' attention'].mean()
            med_avg = df[' meditation'].mean()
            lowGamma_avg = df[' lowGamma'].mean()
            highGamma_avg = df[' highGamma'].mean()
            highAlpha_avg = df[' highAlpha'].mean()
            delta_avg = df[' delta'].mean()
            highBeta_avg = df[' highBeta'].mean()
            lowAlpha_avg = df[' lowAlpha'].mean()
            lowBeta_avg = df[' lowBeta'].mean()
            theta_avg = df[' theta'].mean()
            #chart
            att_chart = list(df[' attention'])
            med_chart = list(df[' meditation'])
            lowGamma_chart = list(df[' lowGamma'])
            highGamma_chart = list(df[' highGamma'])
            highAlpha_chart = list(df[' highAlpha'])
            delta_chart = list(df[' delta'])
            highBeta_chart = list(df[' highBeta'])
            lowAlpha_chart = list(df[' lowAlpha'])
            lowBeta_chart = list(df[' lowBeta'])
            theta_chart = list(df[' theta'])
            #predict
            df = df.T.astype(int)
            att_pred = df.loc[[" attention"]]
            med_pred = df.loc[[" meditation"]]
            lowGamma_pred = df.loc[[" lowGamma"]]
            highGamma_pred = df.loc[[" highGamma"]]
            highAlpha_pred = df.loc[[" highAlpha"]]
            delta_pred = df.loc[[" delta"]]
            highBeta_pred = df.loc[[" highBeta"]]
            lowAlpha_pred = df.loc[[" lowAlpha"]]
            lowBeta_pred = df.loc[[" lowBeta"]]
            theta_pred = df.loc[[" theta"]]
            model = load_model(model_path)
            result_get = model.predict([att_pred,med_pred,lowGamma_pred,highGamma_pred, highAlpha_pred,delta_pred,highBeta_pred,lowAlpha_pred,lowBeta_pred,theta_pred], verbose=0)
            result = result_get[0][0]
            print(result)
            if(result < 0.5):
                lie_persentage = result
                truth_persentage = 1 - result
            elif(result > 0.5):
                truth_persentage = result
                lie_persentage = 1 - result
            else:
                truth_persentage = result
                lie_persentage = result
            #gethistory
            datahistory_global = ""
            if session['level'] == 2:
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM cases")
                datahistory = cur.fetchall()
                cur.close()
                datahistory = datahistory[0:3]
                datahistory_global = datahistory
            else:
                id = session['id']
                idusr = (str(id) + "#" + str(session['username'])).encode('utf-8')
                id_hex = idusr.hex()
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM cases WHERE id_hex_user = %s", (id_hex,))
                datahistory = cur.fetchall()
                cur.close()
                datahistory = datahistory[0:3]
                datahistory_global = datahistory
            #Data kasus
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM cases")
            datacases = cur.fetchall()
            cur.close()
            #return
            return render_template('datadetection.html', shape=df.shape, att_avg=format(att_avg,".2f"), med_avg=format(med_avg,".2f"),
            lowGamma_avg=format(lowGamma_avg,".2f"), highGamma_avg=format(highGamma_avg,".2f"), highAlpha_avg=format(highAlpha_avg,".2f"),
            delta_avg=format(delta_avg,".2f"), highBeta_avg=format(highBeta_avg,".2f"), lowAlpha_avg=format(lowAlpha_avg,".2f"),
            lowBeta_avg=format(lowBeta_avg,".2f"), theta_avg=format(theta_avg,".2f"),
            att_chart=att_chart, med_chart=med_chart, lowGamma_chart=lowGamma_chart, highGamma_chart=highGamma_chart, highAlpha_chart=highAlpha_chart,
            delta_chart=delta_chart, highBeta_chart=highBeta_chart, lowAlpha_chart=lowAlpha_chart, lowBeta_chart=lowBeta_chart, theta_chart=theta_chart,
            truth_persentage=round(truth_persentage*100), lie_persentage=round(lie_persentage*100), datahistory = datahistory_global, datacases = datacases)
        else:
            #gethistory
            datahistory_global = ""
            if session['level'] == 2:
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM cases")
                datahistory = cur.fetchall()
                cur.close()
                datahistory = datahistory[0:3]
                datahistory_global = datahistory
            else:
                id = session['id']
                idusr = (str(id) + "#" + str(session['username'])).encode('utf-8')
                id_hex = idusr.hex()
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM cases WHERE id_hex_user = %s", (id_hex,))
                datahistory = cur.fetchall()
                cur.close()
                datahistory = datahistory[0:3]
                datahistory_global = datahistory
            return render_template('datadetection.html', truth_persentage=100, lie_persentage=100, datahistory = datahistory_global)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = curl.fetchone()
        curl.close()

        if user is not None and len(user) > 0 :
            if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
                session['fullname'] = user['fullname']
                session['email'] = user['email']
                session['username'] = user['username']
                session['id'] = user['id']
                session['level'] = user['level']
                return redirect(url_for('dashboard'))
            else :
                flash("Email dan Password Tidak Cocok")
                return redirect(url_for('login'))
        else :
            flash("User Tidak Ditemukan")
            return redirect(url_for('login'))
    else: 
        return render_template("login.html")
 
@app.route('/adduser', methods=['POST', 'GET']) 
def adduser():
    if 'id' in session:
        if session['level'] == 2:
            if request.method=='GET':
                return render_template('adduser.html')
            else:
                username = request.form['username']
                fullname = request.form['fullname']
                email = request.form['email']
                level = 1
                password = request.form['password'].encode('utf-8')
                hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users (fullname,email,username,password,level) VALUES (%s,%s,%s,%s,%s)" ,(fullname, email, username, hash_password, level)) 
                mysql.connection.commit()

                cur.execute("SELECT * FROM users WHERE email=%s AND username=%s",(email,username,))
                user_new = cur.fetchone()
                user_new_id = user_new['id']

                idusr_new = (str(user_new_id) + "#" + str(username)).encode('utf-8')
                id_usernew_hex = idusr_new.hex()

                cur.execute("UPDATE users SET id_hex=%s WHERE id=%s" ,(id_usernew_hex, user_new_id,)) 
                mysql.connection.commit()

                cur.close()
                flash("You was registration penyidik!")
                return redirect(url_for('adduser'))
        else:
            flash("Bukan hak akses anda!")
            return redirect(url_for('adduser'))
    else:
        return redirect(url_for('login')) 

@app.route('/addcase', methods=['POST', 'GET']) 
def addcase():
    if 'id' in session:
        if request.method=='GET':
            return render_template('addcase.html')
        else:
            fullname = request.form['fullname']
            age = request.form['age']
            gender = request.form['gender']
            subjectcase = request.form['subjectcase']
            now = datetime.now()
            dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
            id_cases = (str(fullname) + "#" + str(age) + "#" + str(dt_string)).encode('utf-8')
            id_hex_cases = id_cases.hex()
            id = session['id']
            idusr = (str(id) + "#" + str(session['username'])).encode('utf-8')
            id_hex_user = idusr.hex()

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO cases (id_hex,id_hex_user,name,age,gender,cases,datetime) VALUES (%s,%s,%s,%s,%s,%s,%s)" ,(id_hex_cases, id_hex_user, fullname, age, gender, subjectcase, dt_string)) 
            mysql.connection.commit()

            cur.close()
            flash("You was registration a new case!")
            return redirect(url_for('addcase'))
    else:
        return redirect(url_for('login')) 

@app.route('/history') 
def history():
    if 'id' in session:
        if session['level'] == 2:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM cases")
            datahistory = cur.fetchall()
            cur.close()
            return render_template('history.html', datahistory = datahistory)
        else:
            id = session['id']
            idusr = (str(id) + "#" + str(session['username'])).encode('utf-8')
            id_hex = idusr.hex()
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM cases WHERE id_hex_user = %s", (id_hex,))
            datahistory = cur.fetchall()
            cur.close()
            return render_template('history.html', datahistory = datahistory)
    else:
        return redirect(url_for('login')) 

@app.route("/detailhistory", methods=["POST","GET"])
def detailhistory():
    if request.method == 'POST':
        idhexcases = request.form['idhexcases']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM interview WHERE id_hex_cases = %s", (idhexcases,))
        detailhistory = cur.fetchall()
        cur.close()
    return jsonify({'htmlresponse': render_template('responsedetail.html',detailhistory=detailhistory)})

@app.route('/saveresult', methods=['GET', 'POST'])
def saveresult():
    if 'id' in session:
        if request.method == 'POST':
            idhexcases = request.form['selectedCases']
            question = request.form['question']
            truth_result = request.form['truth']
            lie_result = request.form['lie']
            now = datetime.now()
            dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
            if (idhexcases or question):
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO interview (id_hex_cases, question, truth, lie, datetime) VALUES (%s,%s,%s,%s,%s)" ,(idhexcases, question, truth_result, lie_result, dt_string))
                mysql.connection.commit()
                cur.close()
                flash("Congratulations! Your data has been saved on the database history prediction!")
                return redirect(url_for('dashboard'))
            else:
                flash("Oh no! Your data can't save, cause there is an empty field!")
                return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

@app.route('/eegextraction', methods=['GET', 'POST'])
def eegextraction():
    if 'id' in session:
        return render_template('eegextraction.html')
    else:
        return redirect(url_for('login'))

@app.route('/downloadfile/<string:namafile>', methods=['GET'])
def downloadfile(namafile):
    if 'id' in session:
        return send_file("static/download/" + namafile, as_attachment=True)
    else:
        return redirect(url_for('login'))

@app.route('/')
def dashboard():
    if 'id' in session:
        if session['level'] == 2:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM cases")
            datahistory = cur.fetchall()
            cur.close()
            datahistory = datahistory[0:3]
            return render_template('datadetection.html', truth_persentage=100, lie_persentage=100, datahistory = datahistory)
        else:
            id = session['id']
            idusr = (str(id) + "#" + str(session['username'])).encode('utf-8')
            id_hex = idusr.hex()
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM cases WHERE id_hex_user = %s", (id_hex,))
            datahistory = cur.fetchall()
            cur.close()
            datahistory = datahistory[0:3]
            return render_template('datadetection.html', truth_persentage=100, lie_persentage=100, datahistory = datahistory)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login')) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)