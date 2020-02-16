from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import subprocess
app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'suagrawal'
#app.config['MYSQL_PASSWORD'] = 'suagrawal'
app.config['MYSQL_DB'] = 'dla_tutorial'

mysql = MySQL(app)

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        text = details['fname']
        number = details['lname']
        print("text ", text)
        print("number ", number)
        date = "12, AUGUST, 2004"
        date1 = "2004-08-12"
        cur = mysql.connection.cursor()
        if checkTableExists(mysql.connection, "p_ridg$lbp_age"): cur.execute("delete from p_ridg$lbp_age")
        if checkTableExists(mysql.connection, "suagarwal_new_input"): cur.execute("delete from suagarwal_new_input")
        if checkTableExists(mysql.connection, "feat$cat_met_a30_2000_cp_w$suagarwal_new_input$user_id$1gra"): cur.execute("delete from feat$cat_met_a30_2000_cp_w$suagarwal_new_input$user_id$1gra")
        if checkTableExists(mysql.connection, "feat$1gram$suagarwal_new_input$user_id$16to16"): cur.execute("delete from feat$1gram$suagarwal_new_input$user_id$16to16")
        mysql.connection.commit()
        cur.execute("INSERT INTO suagarwal_new_input(user_id, date, created_time, message) VALUES (%s, %s, %s, %s)", (number, date, date1, text))
        #cur.execute("INSERT INTO suagarwal_new_input(user_id, date, created_time, message) VALUES (%s, %s, %s, %s)", (number, date, date1, text))
        #cur.execute("INSERT INTO suagarwal_new_input(user_id, date, created_time, message) VALUES (%s, %s, %s, %s)", (number, date, date1, text))

        subprocess.call("./ngramFeature.sh", shell=True)
        subprocess.call("./topicFeature.sh", shell=True)
        subprocess.call("bash runModel.sh", shell=True)
        query_string = "select age from p_ridg$lbp_age where user_id = %s"
        cur.execute(query_string, (number,))
        data = cur.fetchall()
 

        mysql.connection.commit()
        cur.close()
        output = str(data)
        return output
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
