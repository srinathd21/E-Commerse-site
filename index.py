from flask import Flask,render_template,redirect,url_for,request,flash,session
import sqlite3

app = Flask(__name__)
app.secret_key="123"

con = sqlite3.connect("Electro.db")
con.execute("CREATE TABLE IF NOT EXISTS electro_db(pid INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)")
con.close()

@app.route("/")
def home():
    return render_template("pro2_home.html")

@app.route("/home_page")
def home_page():
    return redirect (url_for("home"))

@app.route("/realme11")
def realme11():
    return render_template("realme11.html")

@app.route("/asus_tuf")
def asus_tuf():
    return render_template("asus_tuf.html")

@app.route("/login")
def login():
    return render_template("Elcetro_login.html")

@app.route("/cusomer_account")
def cusomer_account():
    return render_template("Electro_base.html")



@app.route('/creat_account', methods=['POST'])
def creat_account():
    if request.method=='POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['pswd']
            con = sqlite3.connect("Electro.db")
            cur = con.cursor()
            cur.execute("INSERT INTO electro_db(name,email,password) values(?,?,?)",(name,email,password))
            con.commit()
            flash("Account Created Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect('/login')
@app.route("/login_customer", methods=['POST'])
def login_customer():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['pswd']
        con = sqlite3.connect("Electro.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from electro_db where email=? and password=?",(email,password))
        data = cur.fetchone()

        if data:
            session["name"]=data["name"]
            return redirect("/cusomer_account")
        else:
            flash("Username and password mismatch","danger")

    return redirect("/login")




if __name__ == ("__main__"):
    app.run(debug=True)