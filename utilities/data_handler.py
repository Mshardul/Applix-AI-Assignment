from datetime import datetime
from pprint import pprint

LOCATIONS = ["Delhi", "Mumbai", "Kolkata", "Chennai"]

def structure_for_chart(data_loc_datasets, time_labels):
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

def structure_for_frontend(records):
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
        "table_data": structure_for_table(data_loc_datasets, time_labels)
    }
