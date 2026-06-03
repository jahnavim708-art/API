from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connection import get_db_connection

app = FastAPI()

# Request body model
class EmployeeRequest(BaseModel):
    name: str

# API endpoint
@app.post("/get-age")
def get_age(emp: EmployeeRequest):
    name = emp.name

    if not name:
        raise HTTPException(status_code=400, detail="Name is required")

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT employee_age FROM employee1 WHERE employee_name = ?"
    cursor.execute(query, (name,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return {
            #"name": name,
            "age": row[0]
        }
    else:
        raise HTTPException(status_code=404, detail="Employee not found")