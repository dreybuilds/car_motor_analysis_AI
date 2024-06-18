import numpy as np
import random
import string
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.ERROR)

# Define the number of data points to generate
num_points = int(input("Enter the number of data points to generate: "))

def generate_alphanumeric_id(length=8, num_points=num_points):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits
    # Generate a list of alphanumeric IDs
    alphanumeric_ids = []
    for _ in range(num_points):
        alphanumeric_id = ''.join(random.choice(characters) for _ in range(length))
        alphanumeric_ids.append(alphanumeric_id)
    return alphanumeric_ids

def values():
    try:
        # Define the ranges for each parameter
        current_range = (0, 50)  # Amps
        speed_range = (0, 3600)  # RPM
        torque_range = (0, 10)   # Nm
        resistance_range = (0.1, 10)  # Ohms
        inductance_range = (0.001, 0.1)  # Henry
        magnetic_field_range = (0, 1.5)  # Tesla
        back_emf_range = (0, 230)  # Volts
        temp_range = (0, 100)  # Celsius

        # Generate random data points for each parameter
        unique_id_values = generate_alphanumeric_id()
        product_id_values = np.random.randint(1, 100, num_points)
        current_values = np.random.uniform(*current_range, num_points)
        speed_values = np.random.uniform(*speed_range, num_points)
        torque_values = np.random.uniform(*torque_range, num_points)
        resistance_values = np.random.uniform(*resistance_range, num_points)
        inductance_values = np.random.uniform(*inductance_range, num_points)
        magnetic_field_values = np.random.uniform(*magnetic_field_range, num_points)
        back_emf_values = np.random.uniform(*back_emf_range, num_points)
        temp_values = np.random.uniform(*temp_range, num_points)

        # Combine all values into a single array
        data_points = np.column_stack((
            unique_id_values,
            product_id_values,
            current_values,
            speed_values,
            torque_values,
            resistance_values,
            inductance_values,
            magnetic_field_values,
            back_emf_values,
            temp_values
        ))
        return data_points
    except Exception as e:
        logging.error(f"Error generating data points: {e}")
