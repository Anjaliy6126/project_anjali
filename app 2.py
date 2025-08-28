from flask import Flask, request, render_template, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your user name'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'studentdb'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()
    return render_template('form.html', students=students)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    branch = request.form['branch']
    city = request.form['city']



    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO students (name, age, branch, city) VALUES (%s, %s, %s, %s)",
                (name, age, branch, city))
    mysql.connection.commit()
    cur.close()

    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
