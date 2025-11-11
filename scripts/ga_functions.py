import io
from json import load, dump
import math


def load_solomon_txt(txt_file):
    """Convert Solomon .txt instance into a JSON-like Python dict (no file writing)."""

    with io.open(txt_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # --- Extract name ---
    instance_name = lines[0]

    # --- Find section indices ---
    vehicle_idx = lines.index('VEHICLE')
    customer_idx = lines.index('CUSTOMER')

    # --- Vehicle data ---
    vehicle_info = lines[vehicle_idx + 2].split()
    max_vehicle_number = int(vehicle_info[0])
    vehicle_capacity = float(vehicle_info[1])

    # --- Parse customer data ---
    customers = []
    for line in lines[customer_idx + 2:]:
        parts = line.split()
        if len(parts) < 7:
            continue
        cust_no = int(parts[0])
        x = float(parts[1])
        y = float(parts[2])
        demand = float(parts[3])
        ready_time = float(parts[4])
        due_time = float(parts[5])
        service_time = float(parts[6])

        customers.append({
            'id': cust_no,
            'x': x,
            'y': y,
            'demand': demand,
            'ready_time': ready_time,
            'due_time': due_time,
            'service_time': service_time
        })

    # --- Build distance matrix ---
    n = len(customers)
    distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dx = customers[i]['x'] - customers[j]['x']
                dy = customers[i]['y'] - customers[j]['y']
                distance_matrix[i][j] = round(math.hypot(dx, dy), 20)

    # --- Build JSON-like dict ---
    json_data = {}

    for c in customers:
        key = "depart" if c['id'] == 0 else f"customer_{c['id']}"
        json_data[key] = {
            "coordinates": {"x": c['x'], "y": c['y']},
            "demand": c['demand'],
            "ready_time": c['ready_time'],
            "due_time": c['due_time'],
            "service_time": c['service_time']
        }

    json_data["distance_matrix"] = distance_matrix
    json_data["instance_name"] = instance_name
    json_data["max_vehicle_number"] = max_vehicle_number
    json_data["vehicle_capacity"] = vehicle_capacity

    return json_data


def merge_rules(rules):
    '''gavrptw.uitls.merge_rules(rules)'''
    is_fully_merged = True
    for round1 in rules:
        if round1[0] == round1[1]:
            rules.remove(round1)
            is_fully_merged = False
        else:
            for round2 in rules:
                if round2[0] == round1[1]:
                    rules.append((round1[0], round2[1]))
                    rules.remove(round1)
                    rules.remove(round2)
                    is_fully_merged = False
    return rules, is_fully_merged

