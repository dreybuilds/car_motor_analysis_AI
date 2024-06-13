import numpy as np
import psycopg2
from psycopg2 import sql

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="random_data",
    user="dreybuilds",
    password="1234",
    host="localhost",  # or the appropriate host for Docker
    port="5432"
)
cur = conn.cursor()

# Define the number of data points to generate
num_points = 10000

# Define the ranges for each parameter
current_range = (0, 50)  # Amps
speed_range = (0, 3600)  # RPM
torque_range = (0, 10)   # Nm
resistance_range = (0.1, 10)  # Ohms
inductance_range = (0.001, 0.1)  # Henry
magnetic_field_range = (0, 1.5)  # Tesla
back_emf_range = (0, 230)  # Volts

# Generate random data points for each parameter
current_values = np.random.uniform(*current_range, num_points)
speed_values = np.random.uniform(*speed_range, num_points)
torque_values = np.random.uniform(*torque_range, num_points)
resistance_values = np.random.uniform(*resistance_range, num_points)
inductance_values = np.random.uniform(*inductance_range, num_points)
magnetic_field_values = np.random.uniform(*magnetic_field_range, num_points)
back_emf_values = np.random.uniform(*back_emf_range, num_points)

# Combine all values into a single array
data_points = np.column_stack((
    current_values,
    speed_values,
    torque_values,
    resistance_values,
    inductance_values,
    magnetic_field_values,
    back_emf_values
))

# Insert data into the database
insert_query = sql.SQL("""
    INSERT INTO data_points (current, speed, torque, resistance, inductance, magnetic_field, back_emf)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

for data_point in data_points:
    cur.execute(insert_query, tuple(data_point))

# Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")
