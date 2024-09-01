from flask import Flask, render_template, flash, request, session, send_file
import warnings
import os
import mysql.connector

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/ServerLogin")
def ServerLogin():
    return render_template('ServerLogin.html')


@app.route("/CollaboratorLogin")
def CollaboratorLogin():
    return render_template('CollaboratorLogin.html')


@app.route("/NewCollaborator")
def NewCollaborator():
    return render_template('NewCollaborator.html')


@app.route("/PatientLogin")
def PatientLogin():
    return render_template('PatientLogin.html')


@app.route("/NewPatient")
def NewPatient():
    return render_template('NewPatient.html')


@app.route("/CallCenterLogin")
def CallCenterLogin():
    return render_template('CallCenterLogin.html')


@app.route("/NewCallCenter")
def NewCallCenter():
    return render_template('NewCallCenter.html')


@app.route("/ResearchLogin")
def ResearchLogin():
    return render_template('ResearchLogin.html')


@app.route("/NewResearch")
def NewResearch():
    return render_template('NewResearch.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/newco", methods=['GET', 'POST'])
def newco():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from colltb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO colltb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','waiting','')")
            conn.commit()
            conn.close()
            flash('Record Saved!')
            return render_template('CollaboratorLogin.html')

        else:
            flash('Already Register Username !')
            return render_template('NewCollaborator.html')


@app.route("/newcall", methods=['GET', 'POST'])
def newcall():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from calltb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO calltb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
            conn.commit()
            conn.close()
            flash('Record Saved!')
            return render_template('CallCenterLogin.html')

        else:
            flash('Already Register Username !')
            return render_template('NewCallCenter.html')


@app.route("/newpatient", methods=['GET', 'POST'])
def newpatient():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from patienttb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO patienttb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','waiting','')")
            conn.commit()
            conn.close()
            flash('Record Saved!')
            return render_template('PatientLogin.html')

        else:
            flash('Already Register Username !')
            return render_template('NewPatient.html')


@app.route("/newre", methods=['GET', 'POST'])
def newre():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from researchtb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO researchtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
            conn.commit()
            conn.close()
            flash('Record Saved!')
            return render_template('ResearchLogin.html')

        else:
            flash('Already Register Username !')
            return render_template('NewResearch.html')


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from usertb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usertb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
            conn.commit()
            conn.close()
            flash('Record Saved!')
            return render_template('UserLogin.html')

        else:
            flash('Already Register Username !')
            return render_template('NewUser.html')


@app.route("/slogin", methods=['GET', 'POST'])
def slogin():
    if request.method == 'POST':
        if request.form['uname'] == 'server' and request.form['password'] == 'server':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM colltb where status='waiting'")
            data = cur.fetchall()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM colltb where status!='waiting'")
            data1 = cur.fetchall()
            return render_template('ServerHome.html', data=data, data1=data1)

        else:
            flash('Username or Password is Incorrect !')
            return render_template('ServerLogin.html')


import pyAesCrypt
import random
import string


def randStr(chars=string.ascii_uppercase + string.digits, N=10):
    return ''.join(random.choice(chars) for _ in range(N))


def encrypt(key, source, des):
    output = des
    pyAesCrypt.encryptFile(source, output, key)
    return output


def decrypt(key, source, des):
    dfile = source.split(".")
    output = des

    pyAesCrypt.decryptFile(source, output, key)
    return output


@app.route("/Approved")
def Approved():
    id = request.args.get('lid')

    pubhex = randStr(chars='abcdef123456')
    key = pubhex

    # sendmail(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update colltb set Status='Active',EncKey='" + str(key) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where status!='waiting'")
    data1 = cur.fetchall()
    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/Reject")
def Reject():
    id = request.args.get('lid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update colltb set Status='Reject'  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where status!='waiting'")
    data1 = cur.fetchall()
    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/ServerHome")
def ServerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where status!='waiting'")
    data1 = cur.fetchall()
    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/SPatient")
def SPatient():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patienttb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patienttb where status!='waiting'")
    data1 = cur.fetchall()
    return render_template('SPatient.html', data=data, data1=data1)


@app.route("/PApproved")
def PApproved():
    id = request.args.get('lid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update patienttb set Status='Active' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patienttb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patienttb where status!='waiting'")
    data1 = cur.fetchall()
    return render_template('SPatient.html', data=data, data1=data1)


@app.route("/PReject")
def PReject():
    id = request.args.get('lid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update patienttb set Status='Reject'  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patienttb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patienttb where status!='waiting'")
    data1 = cur.fetchall()
    return render_template('SPatient.html', data=data, data1=data1)


@app.route("/cologin", methods=['GET', 'POST'])
def cologin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['cname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from colltb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('CollaboratorLogin.html')

        else:

            Status = data[7]
            if Status == "waiting":

                flash('Waiting For Server Approved!')
                return render_template('CollaboratorLogin.html')

            elif Status == "Reject":
                flash('Server Reject!')
                return render_template('CollaboratorLogin.html')


            else:
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='2CollaborationCloudPy')
                cur = conn.cursor()
                cur.execute("SELECT * FROM colltb where username='" + session['cname'] + "'")
                data1 = cur.fetchall()
                return render_template('CollaboratorHome.html', data=data1)


@app.route("/CollaboratorHome")
def CollaboratorHome():
    cname = session['cname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where USerName='" + cname + "'")
    data = cur.fetchall()

    return render_template('CollaboratorHome.html', data=data)


@app.route("/plogin", methods=['GET', 'POST'])
def plogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['pname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from patienttb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('PatientLogin.html')

        else:
            session['pemailid'] = data[3]

            Status = data[7]
            if Status == "waiting":

                flash('Waiting For Server Approved!')
                return render_template('PatientLogin.html')

            elif Status == "Reject":
                flash('Server Reject!')
                return render_template('PatientLogin.html')


            else:
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='2CollaborationCloudPy')
                cur = conn.cursor()
                cur.execute("SELECT * FROM patienttb where username='" + session['pname'] + "'")
                data1 = cur.fetchall()
                return render_template('PatientHome.html', data=data1)


@app.route("/PatientHome")
def PatientHome():
    pname = session['pname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patienttb where USerName='" + pname + "'")
    data = cur.fetchall()
    return render_template('PatientHome.html', data=data)


@app.route("/PSendRequest")
def PSendRequest():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM colltb where Status='Active'")
    data = cur.fetchall()

    pname = session['pname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM requesttb where PatinetName='" + pname + "'")
    data1 = cur.fetchall()

    return render_template('PSendRequest.html', data=data, data1=data1)


@app.route("/SendRequest")
def SendRequest():
    cname = request.args.get('cname')
    email = request.args.get('email')
    pname = session['pname']

    pemail = session['pemailid']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT * from requesttb where PatinetName='" + pname + "'  and CollaName='" + cname + "' ")
    data = cursor.fetchone()
    if data is None:

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO requesttb VALUES ('','" + pname + "','" + pemail + "','" + cname + "','" + email + "','waiting')")
        conn.commit()
        conn.close()
        flash('Request Send..!')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM colltb where  Status='Active'")
        data = cur.fetchall()

        pname = session['pname']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM requesttb where PatinetName='" + pname + "'")
        data1 = cur.fetchall()

        return render_template('PSendRequest.html', data=data, data1=data1)

    else:
        flash('Already Request Send..!')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM colltb where Status='Active' ")
        data = cur.fetchall()

        pname = session['pname']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM requesttb where PatinetName='" + pname + "'")
        data1 = cur.fetchall()

        return render_template('PSendRequest.html', data=data, data1=data1)


@app.route("/CPatientRequest")
def CPatientRequest():
    cname = session['cname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM requesttb where status='waiting' and CollaName='" + cname + "'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM requesttb where status!='waiting' and CollaName='" + cname + "'")
    data1 = cur.fetchall()
    return render_template('CPatientRequest.html', data=data, data1=data1)


@app.route("/Accept")
def Accept():
    id = request.args.get('lid')
    cname = session['cname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update requesttb set Status='Accept' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM requesttb where status='waiting' and CollaName='" + cname + "'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM requesttb where status!='waiting' and CollaName='" + cname + "'")
    data1 = cur.fetchall()
    return render_template('CPatientRequest.html', data=data, data1=data1)


@app.route("/CFileUpload")
def CFileUpload():
    cname = session['cname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT * from requesttb where  CollaName='" + cname + "' and  Status='Accept' ")
    data = cursor.fetchone()
    if data is None:
        flash('Patient List Empty')
        return render_template('CFileUpload.html')
    else:
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT PatinetName FROM requesttb where  CollaName='" + cname + "' and  Status='Accept'")
        data = cur.fetchall()

        return render_template('CFileUpload.html', data=data)


@app.route("/hupload", methods=['GET', 'POST'])
def hupload():
    if request.method == 'POST':
        cname = session['cname']
        pname = request.form['pname']
        dname = request.form['dname']
        date = request.form['date']
        info = request.form['info']

        file = request.files['file']

        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM filetb ")
        data2 = cursor.fetchone()

        if data2:

            conn1 = mysql.connector.connect(user='root', password='', host='localhost',
                                            database='2CollaborationCloudPy')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(id) from filetb")
            da = cursor1.fetchone()
            if da:
                d = da[0]
                print(d)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM filetb where  id ='" + str(d) + "'   ")
            data1 = cursor.fetchone()
            if data1:
                hash1 = data1[13]
                num1 = random.randrange(1111, 9999)
                hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='2CollaborationCloudPy')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO filetb VALUES ('','" + cname + "','" + pname + "','" + dname + "','" + date + "','" +
                    info + "','" + savename + "','','','','','','" + hash1 + "','" + hash2 + "')")
                conn.commit()
                conn.close()

                flash('Record Saved..!')

                return render_template('CFileUpload.html')

        else:

            hash1 = '0'
            num1 = random.randrange(1111, 9999)
            hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))

            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO filetb VALUES ('','" + cname + "','" + pname + "','" + dname + "','" + date + "','" +
                info + "','" + savename + "','','','','','','" + hash1 + "','" + hash2 + "')")
            conn.commit()
            conn.close()

            flash('Record Saved..!')

            return render_template('CFileUpload.html')


@app.route("/CFileInfo")
def CFileInfo():
    cname = session['cname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where CollName='" + cname + "'")
    data = cur.fetchall()
    return render_template('CFileInfo.html', data=data)


@app.route("/PHealthRecord")
def PHealthRecord():
    pname = session['pname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='' ")
    data = cur.fetchall()

    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='Encrypt' ")
    data1 = cur.fetchall()

    return render_template('PHealthRecord.html', data=data, data1=data1)


@app.route("/Encrypt")
def Encrypt():
    fid = request.args.get('fid')
    pname = session['pname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:
        FileName = data[6]

    else:
        return 'Incorrect username / password !'

    filepath = "./static/upload/" + FileName
    head, tail = os.path.split(filepath)

    newfilepath1 = './static/upload/' + str(tail)
    newfilepath2 = './static/Encrypt/' + str(tail)

    pubhex = randStr(chars='abcdef123456')
    key = pubhex
    encrypt(key, newfilepath1, newfilepath2)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update filetb set Status='Encrypt',ENkey='" + str(key) + "' where id='" + fid + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='' ")
    data = cur.fetchall()

    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='Encrypt' ")
    data1 = cur.fetchall()

    flash('File Encrypt..!')
    return render_template('PHealthRecord.html', data=data, data1=data1)


@app.route("/UrlRequest")
def UrlRequest():
    fid = request.args.get('fid')
    pname = session['pname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update filetb set Status='waiting' where id='" + fid + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='' ")
    data = cur.fetchall()

    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='Encrypt' ")
    data1 = cur.fetchall()

    flash('Url Request Send to Server..!')
    return render_template('PHealthRecord.html', data=data, data1=data1)


@app.route("/PUrlInfo")
def PUrlInfo():
    pname = session['pname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='waiting'  ")
    data = cur.fetchall()

    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='SendUrl' ")
    data1 = cur.fetchall()

    return render_template('PUrlInfo.html', data=data, data1=data1)


@app.route("/SUrlRequet")
def SUrlRequet():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where Status='waiting'  ")
    data = cur.fetchall()
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where   Status='SendUrl' ")
    data1 = cur.fetchall()
    return render_template('SUrlRequet.html', data=data, data1=data1)


@app.route("/SendUrl")
def SendUrl():
    fid = request.args.get('fid')
    fname = request.args.get('fname')

    urlnn = 'http://127.0.0.1:5000/static/Encrypt/' + fname

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update filetb set Status='SendUrl',ServerUrl='" + str(urlnn) + "' where id='" + fid + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where Status='waiting'  ")
    data = cur.fetchall()
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where   Status='SendUrl'   ")
    data1 = cur.fetchall()
    return render_template('SUrlRequet.html', data=data, data1=data1)


import hmac
import hashlib
import binascii


def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode
import secrets
import string
import random


def generate_aes_key():
    return secrets.token_bytes(32)  # 256 bits for AES-256


def aes_encrypt(key, plaintext):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    plaintext = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return b64encode(ciphertext).decode('utf-8')


def aes_decrypt(key, ciphertext):
    ciphertext = b64decode(ciphertext)

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_text = unpadder.update(decrypted_text) + unpadder.finalize()

    return unpadded_text.decode('utf-8')


@app.route("/UrlEncrypt")
def UrlEncrypt():
    fid = request.args.get('fid')
    cname = request.args.get('cname')
    pname = session['pname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:
        furl = data[9]

    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  colltb where  username='" + cname + "'")
    data1 = cursor.fetchone()
    if data1:
        ekey = data1[8]

    else:
        return 'Incorrect username / password !'

    generated_key = generate_aes_key()
    print(generated_key)
    print(generated_key.hex())

    num1 = random.randrange(1111, 9999)
    hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))

    orginalstr = furl + "," + str(hash2)

    encrypted_text = aes_encrypt(generated_key, orginalstr.encode('utf-8'))
    print(f'Encrypted: {encrypted_text}')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update filetb set Status='urlEncrypt',UrlKey='" + str(generated_key.hex()) + "',EncryptUrl='" + str(
        encrypted_text) + "' where id='" + fid + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='' ")
    data = cur.fetchall()

    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='Encrypt' ")
    data1 = cur.fetchall()

    flash('Url Encrypt Encrypt..!')
    return render_template('PHealthRecord.html', data=data, data1=data1)


@app.route("/ColRequest")
def ColRequest():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cuserfiletb where status='waiting' and  Cname='"+ session['cname'] +"'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cuserfiletb where status='CollaboratorApproved' and Cname='"+ session['cname'] +"'")
    data1 = cur.fetchall()

    return render_template('ColRequest.html', data=data, data1=data1)


@app.route("/ColApproved")
def ColApproved():
    fid = request.args.get('ufid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("Update cuserfiletb set Status='CollaboratorApproved'  where id='" + fid + "' ")
    conn.commit()
    conn.close()
    return ColRequest()




@app.route("/URequest")
def URequest():
    pname = session['pname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cuserfiletb where status='CollaboratorApproved' and OwnerName='"+ pname +"' ")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cuserfiletb where status='Approved' and   OwnerName='"+ pname +"' ")
    data1 = cur.fetchall()
    return render_template('URequest.html', data=data, data1=data1)


@app.route("/PatApproved")
def PatApproved():
    fid = request.args.get('ufid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  cuserfiletb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:
        prkey = data[4]
        UserName = data[5]
        email = data[8]
    else:
        return 'Incorrect username / password !'



    mailmsg = "Request Id" + fid + "\n Decryptkey: " + prkey

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("update cuserfiletb set Status='Approved'  where id='" +
                   fid + "'")
    conn.commit()
    conn.close()

    sendmail(email, mailmsg)



    return URequest()



@app.route("/PEncrptUrl")
def PEncrptUrl():
    pname = session['pname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where PatientName='" + pname + "' and Status='urlEncrypt' ")
    data = cur.fetchall()
    return render_template('PEncrptUrl.html', data=data)


@app.route("/clogin", methods=['GET', 'POST'])
def clogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['ccname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from calltb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('CallCenterLogin.html')

        else:
            email = data[3]
            session['email'] = email
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='2CollaborationCloudPy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM calltb where username='" + session['ccname'] + "'")
            data1 = cur.fetchall()
            return render_template('CallCenterHome.html', data=data1)


@app.route("/CallCenterHome")
def CallCenterHome():
    ccname = session['ccname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM calltb where USerName='" + ccname + "'")
    data = cur.fetchall()
    return render_template('CallCenterHome.html', data=data)


@app.route("/CCSearch")
def CCSearch():
    return render_template('CCSearch.html')


@app.route("/ccsearch", methods=['GET', 'POST'])
def ccsearch():
    if request.method == 'POST':
        pname = request.form['pname']
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM filetb where PatientName='" + pname + "'")
        data1 = cur.fetchall()
        return render_template('CCSearch.html', data=data1)


@app.route("/SendKeyRequest")
def SendKeyRequest():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        oname = data[2]
        fname = data[6]
        prkey = data[7]

        cname = data[1]

    else:
        return 'Incorrect username / password !'
    
    ccname = session['ccname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Cuserfiletb VALUES ('','" + fid + "','" + oname + "','" + fname + "','" + prkey + "','" + session[
            'ccname'] + "','waiting','callcenter','"+ session['email'] +"','"+ cname +"')")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='waiting' and username='" + session['ccname'] + "' and  Type='callcenter' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='Approved' and username='" + session['ccname'] + "' and  Type='callcenter' ")
    data1 = cur.fetchall()
    return render_template('CCDownload.html', data=data, data1=data1)


@app.route("/CCStatus")
def CCStatus():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='waiting' and username='" + session['ccname'] + "'  and  Type='callcenter'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='Approved' and username='" + session['ccname'] + "' and  Type='callcenter' ")
    data1 = cur.fetchall()
    return render_template('CCDownload.html', data=data, data1=data1)




@app.route("/userdownload")
def userdownload():
    ufid = request.args.get('ufid')

    session["ufid"] = ufid

    return render_template('CDownload.html')


@app.route("/downalod", methods=['GET', 'POST'])
def downalod():
    if request.method == 'POST':
        fid = session["ufid"]
        ekey = request.form['ekey']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  Cuserfiletb where  id='" + fid + "' and  PrKey='" + ekey + "' and  Type='callcenter'")
        data = cursor.fetchone()
        if data:
            prkey = data[4]
            fname = data[3]
            privhex = prkey



            filepath = "./static/Encrypt/" + fname
            head, tail = os.path.split(filepath)

            newfilepath1 = './static/Encrypt/' + str(tail)
            newfilepath2 = './static/Decrypt/' + str(tail)

            decrypt(privhex, newfilepath1, newfilepath2)

            return send_file(newfilepath2, as_attachment=True)



        else:
            return 'Key Incorrect!'


@app.route("/rlogin", methods=['GET', 'POST'])
def rlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['rccname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from researchtb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('ResearchLogin.html')

        else:
            email = data[3]
            session['email'] = email
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='2CollaborationCloudPy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM researchtb where username='" + session['rccname'] + "'")
            data1 = cur.fetchall()
            return render_template('ResearchHome.html', data=data1)


@app.route("/ResearchHome")
def ResearchHome():
    rccname = session['rccname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM researchtb where USerName='" + rccname + "'")
    data = cur.fetchall()
    return render_template('ResearchHome.html', data=data)


@app.route("/CCSearch1")
def CCSearch1():
    return render_template('CCSearch1.html')


@app.route("/ccsearch1", methods=['GET', 'POST'])
def ccsearch1():
    if request.method == 'POST':
        pname = request.form['pname']
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM filetb where DiseaseName='" + pname + "'")
        data1 = cur.fetchall()
        return render_template('CCSearch1.html', data=data1)


@app.route("/SendKeyRequest1")
def SendKeyRequest1():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        oname = data[2]
        fname = data[6]
        prkey = data[7]
        cname = data[1]

    else:
        return 'Incorrect username / password !'

    rccname = session['rccname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Cuserfiletb VALUES ('','" + fid + "','" + oname + "','" + fname + "','" + prkey + "','" + session[
            'rccname'] + "','waiting','Research','" + session['email'] + "','"+ cname +"')")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='waiting' and username='" + session['rccname'] + "' and  Type='Research' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='Approved' and username='" + session['rccname'] + "' and  Type='Research' ")
    data1 = cur.fetchall()
    return render_template('CCDownload1.html', data=data, data1=data1)


@app.route("/CCStatus1")
def CCStatus1():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='waiting' and username='" + session['rccname'] + "' and  Type='Research' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='Approved' and username='" + session['rccname'] + "' and  Type='Research' ")
    data1 = cur.fetchall()
    return render_template('CCDownload1.html', data=data, data1=data1)


@app.route("/userdownload1")
def userdownload1():
    ufid = request.args.get('ufid')

    session["ufid"] = ufid

    return render_template('CDownload1.html')


@app.route("/downalod1", methods=['GET', 'POST'])
def downalod1():
    if request.method == 'POST':
        fid = session["ufid"]
        ekey = request.form['ekey']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  Cuserfiletb where  id='" + fid + "' and  PrKey='" + ekey + "' and   Type='Research'")
        data = cursor.fetchone()
        if data:
            prkey = data[4]
            fname = data[3]
            privhex = prkey

            filepath = "./static/Encrypt/" + fname
            head, tail = os.path.split(filepath)

            newfilepath1 = './static/Encrypt/' + str(tail)
            newfilepath2 = './static/Decrypt/' + str(tail)

            decrypt(privhex, newfilepath1, newfilepath2)

            return send_file(newfilepath2, as_attachment=True)



        else:
            return 'Key Incorrect!'





@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['uccname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from usertb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')

        else:
            email = data[3]
            session['email'] = email
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='2CollaborationCloudPy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM usertb where username='" + session['uccname'] + "'")
            data1 = cur.fetchall()
            return render_template('UserHome.html', data=data1)


@app.route("/UserHome")
def UserHome():
    uccname = session['uccname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM usertb where USerName='" + uccname + "'")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/CCSearch2")
def CCSearch2():
    return render_template('CCSearch2.html')


@app.route("/ccsearch2", methods=['GET', 'POST'])
def ccsearch2():
    if request.method == 'POST':
        pname = request.form['pname']

        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='2CollaborationCloudPy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM filetb where DiseaseName='" + pname + "' or PatientName ='"+ pname +"'")
        data1 = cur.fetchall()
        return render_template('CCSearch2.html', data=data1)


@app.route("/SendKeyRequest2")
def SendKeyRequest2():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        oname = data[2]
        fname = data[6]
        prkey = data[7]
        cname = data[1]

    else:
        return 'Incorrect username / password !'

    uccname = session['uccname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Cuserfiletb VALUES ('','" + fid + "','" + oname + "','" + fname + "','" + prkey + "','" + session[
            'uccname'] + "','waiting','User','" + session['email'] + "','"+ cname +"')")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='waiting' and username='" + session['uccname'] + "' and  Type='User' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='Approved' and username='" + session['uccname'] + "' and  Type='User' ")
    data1 = cur.fetchall()
    return render_template('CCDownload2.html', data=data, data1=data1)


@app.route("/CCStatus2")
def CCStatus2():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='waiting' and username='" + session['uccname'] + "' and  Type='User' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cuserfiletb where status='Approved' and username='" + session['uccname'] + "' and  Type='User' ")
    data1 = cur.fetchall()
    return render_template('CCDownload2.html', data=data, data1=data1)


@app.route("/userdownload2")
def userdownload2():
    ufid = request.args.get('ufid')

    session["ufid"] = ufid

    return render_template('CDownload2.html')


@app.route("/downalod2", methods=['GET', 'POST'])
def downalod2():
    if request.method == 'POST':
        fid = session["ufid"]
        ekey = request.form['ekey']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2CollaborationCloudPy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  Cuserfiletb where  id='" + fid + "' and  PrKey='" + ekey + "' and   Type='User'")
        data = cursor.fetchone()
        if data:
            prkey = data[4]
            fname = data[3]
            privhex = prkey

            filepath = "./static/Encrypt/" + fname
            head, tail = os.path.split(filepath)

            newfilepath1 = './static/Encrypt/' + str(tail)
            newfilepath2 = './static/Decrypt/' + str(tail)

            decrypt(privhex, newfilepath1, newfilepath2)

            return send_file(newfilepath2, as_attachment=True)



        else:
            return 'Key Incorrect!'


def sendmsg(targetno, message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")






















def sendmail(Mailid,message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qmgn xecl bkqv musr")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

if __name__ == '__main__':
    # app.run(host='0.0.0.0',debug = True, port = 5000)
    app.run(debug=True, use_reloader=True)
