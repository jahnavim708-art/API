#flask
from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=your_database;"
    "Trusted_Connection=yes;"
    )
    return conn


@app.route('/get-age', methods=['POST'])
def get_age():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT employee_age FROM employee1 WHERE employee_name = ?"
    cursor.execute(query, (name,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return jsonify({
            "name": name,
            "age": row[0]
        })
    else:
        return jsonify({"error": "Employee not found"}), 404
 
if __name__ == '__main__':
    app.run(debug=True)     