import pandas as pd
from django.utils.dateformat import re_escaped


def read_and_parse_file(file_path):
    raw_readings = []
    with open(file_path, "r") as file:
        for line in file:
            # Strip whitespace/newline characters and split by comma
            parts = line.strip().split(",")
            if len(parts) == 3:
                sensor_id = parts[0]
                temp_str = parts[1]
                timestamp = parts[2]

                # Convert temperature string to float or None
                if temp_str == "None" or temp_str == "":
                    temp_val = None
                else:
                    temp_val = float(temp_str)

                # Store as a tuple (sensor_id, temperature, timestamp)
                raw_readings.append((sensor_id, temp_val, timestamp))
    return raw_readings

def clean_sensor_data(file_path):
    raw_inputs = read_and_parse_file(file_path)
    valid_data = {}     #Create a dictionary
    if raw_inputs:
        for sensor_id, temp_val, timestamp in raw_inputs:
            #Filter out invalid temperature measurements
            if temp_val is not None and -40.0 <= temp_val <= 120.0:
                if sensor_id not in valid_data:
                    valid_data[sensor_id] = []
                valid_data[sensor_id].append(temp_val)
    #Define a summary dictionary
    calculate_table = {}
    for sensor_id, temp_vals in valid_data.items():
        count = len(temp_vals)
        if count > 0:
            total_sum = 0
            for total_count in temp_vals:
                total_sum += total_count
            average = total_sum / count
            calculate_table[sensor_id] = {'average': average, 'count': count}

    return calculate_table

clean = clean_sensor_data("sensor_data.txt")
print(clean)


#Question 2: Solar Battery Simulator
print()
print("------Q2: Solar Battery Simulator------")
print()

initial_soc = float(input("Please enter initial SOC: "))
max_capacity = float(input("Please enter maximum capacity: "))
hourly_data = [
 (0.0, 1.2), (0.0, 1.1), (0.0, 1.0), (0.0, 1.2), # Hours 0-3 (Night)
 (-2, 1.5), (1.5, 2.0), (-2, 1.8), (5.5, 2.1), # Hours 4-7 (Morning)
 (8.0, 2.2), (9.5, 2.5), (10.0, 2.8), (9.0, 2.4), # Hours 8-11 (Midday)
 (7.5, 2.0), (5.0, 1.8), (3.0, 1.6), (1.0, 2.2), # Hours 12-15 (Afternoon)
 (0.2, 3.0), (999.0, 3.5), (0.0, 2.8), (0.0, 2.0), # Hours 16-19 (Evening)
 (0.0, 1.8), (-2.0, 1.5), (0.0, 1.3), (0.0, 1.2) # Hours 20-23 (Night)
]

for solar_generation, home_demand in hourly_data:
    net_soc = solar_generation - home_demand
total_wasted = 0.0
total_grid_import = 0.0
hourly_states = []

current_soc = initial_soc
if current_soc > max_capacity:
    surplus = current_soc - max_capacity
    total_wasted += surplus
    current_soc = max_capacity
    status = 'wasted'
elif current_soc < 0:
    deficit = abs(current_soc)
    total_grid_import += deficit
    current_soc = 0
    status = 'grid-import'
else:
    status = 'normal'

for t, (solar_generation, home_demand) in enumerate(hourly_data):
    if solar_generation < 0 or home_demand < 0:
        print(f"Sensor fault detected at Hour{t}/ Skipping calculation")
        continue
    if solar_generation == 999.0:
        print(f"Grid shutdown signal detected at Hour{t}. Terminating calculation")
        break

    hourly_states.append({'hour': t, 'soc': current_soc, 'status': status})

printer = {
    'hourly_states': hourly_states,
    'total_wasted': total_wasted,
    'total_grid_import': total_grid_import,
}
print(printer)


#Question 3: Wind Turbine Performance Analysis
print()
print("------Q3: Wind Turbine Performance Analysis------")
print()

def analyze_turbine_data(file_path):
    fileread = pd.read_csv(file_path)
    wind_speed = fileread['Wind_Speed']

    def status_check(wind_speed):
        if wind_speed < 3.0 or wind_speed > 15.0:
            return 'Offline'
        return 'Active'

    fileread['Expected_Status'] = fileread['Wind_Speed'].apply(status_check)

    finalFile = fileread[fileread['Expected_Status'] == 'Active']

    group_data = []
    unique_turbine = finalFile['Turbine_ID'].unique()
    for turbine_id in unique_turbine:
        turbine_data = finalFile[finalFile['Turbine_ID'] == turbine_id]

        #Calculation mean
        mean_wild = turbine_data['Wind_Speed'].mean()
        mean_power = turbine_data['Power_Output'].mean()
        group_data.append({'Turbine ID': turbine_id, 'Wind Speed': mean_wild, 'Power Output': mean_power})

    final_read = pd.DataFrame(group_data)
    final_read.to_csv('active_turbine_summary.csv', index=False)

    return final_read
read = analyze_turbine_data('wind_turbine_data.csv')
print(read)