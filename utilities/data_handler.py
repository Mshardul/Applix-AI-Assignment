# External Libaries
from datetime import datetime
import numpy as np
import pandas as pd
from pprint import pprint
from scipy import stats

LOCATIONS = ["Delhi", "Mumbai", "Kolkata", "Chennai"]

def stats_calculations(valid_temperatures):
    """ calculate statistics on an numpy array """
    # Statistics Calculation
    mean_temp = np.mean(valid_temperatures)
    median_temp = np.median(valid_temperatures)
    mode_temp = stats.mode(valid_temperatures, keepdims=True)[0][0]  # Extract mode value
    min_temp = np.min(valid_temperatures)
    max_temp = np.max(valid_temperatures)

    # Trend (Simple Linear Regression) Computation
    x = np.arange(len(valid_temperatures))  # Time steps
    slope, _ = np.polyfit(x, valid_temperatures, 1)  # Linear fit
    trend = "Increasing" if slope > 0 else "Decreasing" if slope < 0 else "Stable"

    # Return Response
    return {
        "Mean": round(mean_temp, 2),
        "Median": round(median_temp, 2),
        "Mode": round(mode_temp, 2),
        "Min": round(min_temp, 2),
        "Max": round(max_temp, 2),
        "Trend": trend
    }

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
