"""
RECORD CHECK
Name  : Shiv Rami
Lane  : AI / Data Science
Date  : 24/10/2026
"""

import os


class Record:
    def __init__(self, label, value, limit):
        """Store the label, value and limit for this record."""
        self.dataset_name = label
        self.rows_loaded = value
        self.rows_expected = limit

    def status(self):
        """Return the status based on rows loaded versus expected."""
        percent = (self.rows_loaded / self.rows_expected) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read records from a file and return them as Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            label = parts[0]
            value = float(parts[1])
            limit = float(parts[2])
            records.append(Record(label, value, limit))

    return records


data_path = os.path.join(os.path.dirname(__file__), "ai_records.txt")
records = load_records(data_path)
over_limit_count = 0

for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.dataset_name}")
    print("=" * 34)
    print(f"  Rows loaded  : {record.rows_loaded}")
    print(f"  Rows expected: {record.rows_expected}")
    print(f"  Status       : {status}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"{over_limit_count} of {len(records)} records are OVER LIMIT")
