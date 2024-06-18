import numpy as np
import psycopg2
from psycopg2 import sql
from gen_rand import *
import yaml

# Read the YAML configuration file
with open('/home/dreybuilds/Documents/dev/car_motor_analysis_AI/rand/db_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Get the database connection parameters
db_params = config['database']

# Connect to the database
conn = psycopg2.connect(**db_params)
# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname=db_params['dbname'],
    user=db_params['user'],
    password=db_params['password'],
    host=db_params['host'],
    port=db_params['port']

)
cur = conn.cursor()
def create_table():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL statement to create the table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS data_points1 (
            unique_id VARCHAR(255) PRIMARY KEY,
            product_id INTEGER,
            current DECIMAL,
            speed DECIMAL,
            torque DECIMAL,
            resistance DECIMAL,
            inductance DECIMAL,
            magnetic_field DECIMAL,
            back_emf DECIMAL,
            temp DECIMAL
        );
        """

        # Execute the create table query
        cur.execute(create_table_query)
        conn.commit()

        logging.info("Table 'data_points' created successfully in database 'random_data'.")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        logging.error(f"Error creating table: {e}")

# Call create_table to execute the table creation process
create_table()

# Insert data into the database
insert_query = sql.SQL("""
    INSERT INTO data_points1 (unique_id, product_id,current, speed, torque, resistance, inductance, magnetic_field, back_emf,temp)
    VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
""")

for data_point in values():
    try:
        print(data_point)
        cur.execute(insert_query, tuple(data_point))
    except Exception as e:
        print(f"Error inserting data: {e}")

# Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")
