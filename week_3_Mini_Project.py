"""
RECORD CHECK  -  my version
===========================

Name  : Shiv Rami
Lane  :  AI
Date  : 09/10/2026
Run it: python template.py
"""

def status_of(percent):
    if percent >= 100:
        return("OVER LIMIT")
    elif percent >= 90:
        return ("Warning")
    else:
        return ("OK")

def check(value, limit):
    difference = limit - value
    percent = value / limit * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Loaded  : {value:>10.2f}")
    print(f"Expected: {limit:>10.2f}")
    print(f"Missing : {difference:>10.2f}")
    print(f"Percent : {percent:>10.2f} %")
    print(f"Status  : {status:>10}")
    print("=" * 34)

over_limit_count = 0
while True:
    label = input("Dataset name (type quit to stop): ")
    if label == "quit":
        
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))
    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit_count = over_limit_count + 1
    print_report(label, value, limit, difference, percent, status)
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print("=" * 34)
print()