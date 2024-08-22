import json
import pandas as pd
from collections import defaultdict

# Sample response JSON
response_json = '''
{
    "responsePayload": {
        "patient_details": [
            {"User": "User1", "Patient": "Patient1", "Time In": "2024-07-01", "Form Date": "2024-07-01", "Details": "Details1"},
            {"User": "User2", "Patient": "Patient2", "Time In": "2024-07-02", "Form Date": "2024-07-02", "Details": "Details2"},
            {"User": "User1", "Patient": "Patient1", "Time In": "2024-07-03", "Form Date": "2024-07-03", "Details": "Details3"}
        ]
    }
}
'''

# Load the JSON object
response_obj = json.loads(response_json)
patient_details = response_obj["responsePayload"]["patient_details"]

print("patient_details -> ",patient_details)
# Grouping patients
grouped_patients = defaultdict(list)
for patient in patient_details:
    key = (patient["User"], patient["Patient"], patient["Time In"], patient["Form Date"])
    grouped_patients[key].append(patient)

print("grouped_patients -> ", grouped_patients)
# Select the first item from each group
selected_patients = [patients[0] for patients in grouped_patients.values()]

print("selected_patients -> ", selected_patients)

# Convert the result to a JSON array
result_json_array = json.dumps(selected_patients, indent=4)

# print(result_json_array)

