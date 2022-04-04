"""waf to fetch data from sql table via api"""

"""
1.import sqlite3
2.connect to db
3.cursor
4.cursor.excute
5.db.commit()
6.db.close()
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/task1/fetchdata", methods=['GET', 'POST'])
def fetch_data():
    if request.method == 'POST':
        database_name = request.json['dbname']
        table = request.json['table_name']
        # connect to db
        db = sqlite3.connect(database_name)
        # cursor
        cursor = db.cursor()
        # create table
        cursor.execute('''create table ''' + table + '''
                            (name text , empid int , location text , cgpa real)
                        ''')

        cursor.execute("insert into "+ table + " values('Gyana', 1029045, 'BBSR', 8.3)")

        cursor.execute("insert into "+ table + " values('Sid',10000,'UK',8.3)")

        cursor.execute("insert into "+ table + " values('swadhin',10001,'BBSR',8.3)")

        cursor.execute("insert into "+ table + " values('Chandan',10002,'RLK',8.3)")
        db.commit()

        query = "select * from " + str(table)
        data = cursor.execute(query)
        return jsonify(data.fetchall())


if __name__ == '__main__':
    app.run(port=8000)

    """
    --in postman
    {
    "dbname":"ineuron.db" ,
    "table_name":"employee"
    }
    """
