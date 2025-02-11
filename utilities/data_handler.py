""" Data Hander Utility Functions """

# Standard Libraries Import
from pprint import pprint

# External Libaries Import
from datetime import datetime
import numpy as np
from scipy import stats

LOCATIONS = ["Delhi", "Mumbai", "Kolkata", "Chennai"]

def stats_calculations(valid_temperatures):
    """ calculate statistics on an numpy array """
    # default values
    resp = {
        "Mean": "N/A",
        "Median": "N/A",
        "Mode": "N/A",
        "Min": "N/A",
        "Max": "N/A",
        "Trend": "N/A"
    }
    if len(valid_temperatures)==0:
        return resp

    # Statistics Calculation
    resp["Mean"] = round(np.mean(valid_temperatures), 2)
    resp["Median"] = round(np.median(valid_temperatures))
    resp["Mode"] = round(stats.mode(valid_temperatures, keepdims=True)[0][0], 2)
    resp["Min"] = round(np.min(valid_temperatures), 2)
    resp["Max"] = round(np.max(valid_temperatures), 2)

    # Trend (Simple Linear Regression) Computation
    try:
        x = np.arange(len(valid_temperatures))  # Time steps
        slope, _ = np.polyfit(x, valid_temperatures, 1)  # Linear fit
        resp["Trend"] = "Increasing" if slope > 0 else "Decreasing" if slope < 0 else "Stable"
    except np.linalg.LinAlgError:
        resp["Trend"] = "N/A"

    # Return Response
    return resp

def structure_for_chart(data_loc_datasets, time_labels):
    """ strucutre temperature data for chart-friendly import """
    datasets = []
    for location in LOCATIONS:
        datasets.append({
            "label": location,
            "data": data_loc_datasets[location],
        })
    return {
        "labels": time_labels,
        "datasets": datasets
    }

def structure_for_table(data_loc_datasets, time_labels):
    """ strucutre temperature data for table-friendly import """
    resp = []
    n: int = len(time_labels)
    ind = 0
    while ind<n:
        time_label = time_labels[ind]
        for location in LOCATIONS:
            temp = data_loc_datasets[location][ind]
            if temp is not None:
                resp.append({
                    "id": f"{location}__{time_label}",
                    "time": time_label,
                    "temperature": temp,
                    "location": location
                })
        ind += 1
    return resp

def structure_for_stats(data_loc_datasets):
    """ strucutre temperature data for stats-friendly import """
    resp: list[dict] = []
    for city, temperatures in data_loc_datasets.items():
        valid_temperatures = [temp for temp in temperatures if temp is not None]
        if not temperatures:
            continue

        valid_temperatures = np.array(valid_temperatures)
        statistics_data: dict = stats_calculations(valid_temperatures)

        statistics_data["id"] = city
        statistics_data["City"] = city
        resp.append(statistics_data)

    return resp

def structure_for_frontend(records):
    """ strucutre temperature data for frontend [chart, table, statistics] """
    def structure_data_by_time_loc_temp(records):
        data_time_loc_temp = {}
        for record in records:
            time_int = record.get('time', '')
            location = record.get('location', '')
            temperature = record.get('temperature', None)

            time_str = datetime.utcfromtimestamp(time_int).strftime('%Y-%m-%d %H:%M:%S')

            if time_str not in data_time_loc_temp:
                data_time_loc_temp[time_str] = {}
            data_time_loc_temp[time_str][location] = temperature
        return data_time_loc_temp

    def structure_data_by_loc_dataset(data_time_loc_temp, time_labels):
        """ { location -> [temp_reading] } """
        data_loc_datasets:dict[str, list[float]] = {location: [] for location in LOCATIONS}
        for time_label in time_labels:
            data_loc_temp = data_time_loc_temp.get(time_label)
            for location in LOCATIONS:
                data_loc_datasets[location].append(data_loc_temp.get(location, None))
        return data_loc_datasets

    data_time_loc_temp = structure_data_by_time_loc_temp(records)
    print("*"*3, "1", "*"*3)
    pprint(data_time_loc_temp)

    time_labels: list[str] = list(sorted(set(data_time_loc_temp.keys())))
    print("*"*3, "2", "*"*3)
    pprint(time_labels)

    data_loc_datasets: dict[str, list[float]] = structure_data_by_loc_dataset(data_time_loc_temp, time_labels)
    print("*"*3, "3", "*"*3)
    pprint(data_loc_datasets)
    return {
        "chart_data": structure_for_chart(data_loc_datasets, time_labels),
        "table_data": structure_for_table(data_loc_datasets, time_labels),
        "stats_data": structure_for_stats(data_loc_datasets)
    }
