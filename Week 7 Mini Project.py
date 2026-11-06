"""
RECORD CHECK - my version
===========================

Name: Shiv Rami
Lane: AI / Data Science
Date: 6/11/2026

Ratings below 3 are flagged for review.
"""

from pathlib import Path

def parse_line(raw_line):
    """Clean one survey line and return its fields as a dictionary."""
    line = raw_line.strip().lower()
    survey_part, rest = line.split(",", 1)
    survey = survey_part.strip()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip()] = float(value.strip())

    return {"survey": survey, **fields}

def status_of(record):
    """Flag survey ratings below 3 and return OK for the others."""
    if record["rating"] < 3:
        return "FLAGGED"
    return "OK"

input_count = 0
valid_count = 0
flagged_count = 0

data_path = Path(__file__).with_name("W7_data.txt")
with data_path.open(encoding="utf-8") as data_file:
    for raw_line in data_file:
        if not raw_line.strip():
            continue

        input_count += 1
        try:
            record = parse_line(raw_line)
        except ValueError as error:
            print(f"Could not parse record: {error}")
            continue

        status = status_of(record)
        valid_count += 1
        if status == "FLAGGED":
            flagged_count += 1

        print(record, "-", status)

print(
    f"Summary: {input_count} input records, {valid_count} valid, "
    f"{flagged_count} flagged."
)
