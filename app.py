# ------------------------- IMPORTS -------------------------
import json
from flask import Flask, jsonify
import random
import mysql.connector

# ------------------------- CONSTANTS -------------------------
HOST = "localhost"
USER = "root"
PASSWORD = "***************************"

# ------------------------- CONNECT TO MySQL -------------------------
connection = mysql.connector.connect(
    host = HOST,
    user = USER,
    password = PASSWORD
)
mycursor = connection.cursor()
mycursor.execute("USE competitors_database;")
mycursor.execute("SELECT * FROM competitors_table")

# ------------------------- HELPER VARIABLE -------------------------
lastId = len(mycursor.fetchall())
mycursor.close()

# ------------------------- CREATE FLASK APPLICATION -------------------------
app = Flask(__name__)

# ------------------------- INDEX (READ / GET) -------------------------
@app.route('/', methods=['GET'])
def index():
    '''This method loads the home screen.'''
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    mycursor = connection.cursor()
    mycursor.execute("USE competitors_database;")
    mycursor.execute("SELECT * FROM competitors_table;")
    competitors = mycursor.fetchall()
    mycursor.close()
    return jsonify(competitors), 200

# ------------------------- CREATE / POST -------------------------
@app.route('/create/<string:name>/', methods=['GET', 'POST'])
def add_competitor(name):
    '''This method takes in a name and adds it to the list of competitors.'''
    global lastId
    nextId = lastId + 1
    lastId += 1
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    mycursor = connection.cursor()
    mycursor.execute("USE competitors_database;")
    mycursor.execute(f"INSERT INTO competitors_table(id, name) VALUES ({nextId}, '{name}');") # Entry is added to the end of the table
    mycursor.execute("SELECT * FROM competitors_table;")
    competitors = mycursor.fetchall()
    connection.commit()     # Save
    mycursor.close()
    return jsonify(competitors), 200

# ------------------------- READ / GET -------------------------
@app.route('/read/<int:id>/')
def get_competitor(id):
    '''
    This method takes in an id and reads the name of that competitor.
    If no id was given, a random competitor's name is returned.
    '''
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    mycursor = connection.cursor()
    mycursor.execute("USE competitors_database;")
    mycursor.execute("SELECT * FROM competitors_table;")
    competitors = mycursor.fetchall()

    # Cases where id is valid, we return the competitor:
    for competitor in competitors:
        if competitor[0] == id:
            mycursor.close()
            return jsonify(competitors[id - 1]), 200

    # Cases where id isn't valid, we throw a 404 error:
    mycursor.close()
    return "404 error. The requested id was not found on this server.", 404

# ------------------------- UPDATE / PUT -------------------------
@app.route('/update/<int:id>/<string:name>/', methods=['GET', 'POST'])
def update_competitor(id, name):
    '''This method takes in an id and updates that competitor's name.'''
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    mycursor = connection.cursor()
    mycursor.execute("USE competitors_database;")
    mycursor.execute("SELECT * FROM competitors_table")
    competitors = mycursor.fetchall()

    for competitor in competitors:
        if competitor[0] == id:
            mycursor.execute(f"UPDATE competitors_table SET name = '{name}' WHERE id = {id};")
            mycursor.execute("SELECT * FROM competitors_table")
            competitors = mycursor.fetchall()
            connection.commit()     # Save
            mycursor.close()
            return jsonify(competitors), 200
    return "404 error. The requested id was not found on this server.", 404

# ------------------------- DELETE -------------------------
@app.route('/delete/<int:id>/', methods=['GET', 'DELETE'])
def delete_competitor(id):
    '''This method takes an id and deletes the corresponding entry.'''
    global lastId
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    mycursor = connection.cursor(buffered=True)
    mycursor.execute("USE competitors_database;")
    mycursor.execute("SELECT * FROM competitors_table")
    competitors = mycursor.fetchall()

    for competitor in competitors:
        if competitor[0] == id:
            # Remove the competitor
            mycursor.execute(f"DELETE FROM competitors_table WHERE id = {id};")

            # Update all of the ids of the remaining competitors
            for i in range(id, len(competitors)):
                mycursor.execute(f"UPDATE competitors_table SET id = {i} WHERE id = {i + 1};")

            mycursor.execute("SELECT * FROM competitors_table")
            competitors = mycursor.fetchall()
            connection.commit()  # Save
            mycursor.close()
            return jsonify(competitors), 200
    # Handle cases where id is not found:
    mycursor.close()
    return "404 error. The requested id was not found on this server.", 404

# ------------------------- RUN FLASK APP -------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# ------------------------- URLS -------------------------
# Index URL:            http://localhost:5000/
# Create / Post:        http://localhost:5000/create/<name>
# Read / Get:           http://localhost:5000/read/<id>
# Update / Put:         http://localhost:5000//update/<id>/<name>
# Delete:               http://localhost:5000/delete/<id>