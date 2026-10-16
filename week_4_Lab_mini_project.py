"""
RECORD CHECK  -  my version
===========================

Name  : Shiv Rami
Lane  :  AI
Date  : 16/10/2026

"""
def check_record(value, limit):
    """Work out the difference, percent and status for one record."""
    difference = value - limit
    percent = value / limit * 100
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percent, status
 
def print_report(record, difference, percent, status):
    """Print the report for one record."""
    print("Dataset   :", record["label"])
    print("Loaded    :", record["value"], "of", record["limit"])
    print("Difference:", difference)
    print("Percent   :", round(percent, 1), "%")
    print("Status    :", status)
    print("-" * 30)
 
def load_records(path):
    records = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line != "":
                label, value, limit = line.split(",")
                records.append({"label": label, "value": int(value), "limit": int(limit)})
    return records
 
def save_results(path, lines):
    """Write each line in the list to a new file."""
    with open(path, "w") as file:
        for line in lines:
            file.write(line + "\n")
 
try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("Could not find records.txt - starting with an empty list.")
    records = []
 
result_lines = []
over_count = 0      
 
for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record, difference, percent, status)
 
    result_lines.append(record["label"] + "," + status)
    if status == "OVER LIMIT":
        over_count = over_count + 1
 
print("Records over limit:", over_count)
 
save_results("results.txt", result_lines)
print("Results saved to results.txt")
 