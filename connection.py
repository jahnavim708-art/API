from sqlalchemy import create_engine

DATABASE_URL = (
    "mssql+pyodbc://localhost\\SQLEXPRESS/employee"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

def get_db_connection():
    return engine