import pandas as pd
from sqlalchemy import create_engine

# Database credentials
host = "localhost"         # Change if phpMyAdmin runs on a different host
user = "root"              # Default phpMyAdmin user
password = ""              # Set your MySQL password
database = "library" # Replace with your database name

# Create database connection
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
# engine = create_engine("mysql+pymysql://root:@localhost/library")

# Read table into pandas DataFrame
table_name = "admin"  # Replace with your table name
df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)

# Display the data
print(df)
print(pd.read_sql(f"SELECT * FROM tblstudents", con=engine))
