"""
RECORD CHECK - 
Name: Shiv Rami
Lane: AI / Data Science
Date: 30 October 2026

Run from this folder with: python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ai_dataset_records.csv")

# Compare the number of rows loaded with the expected number for each dataset.
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
print(df)

not_ok = df[df["status"] != "OK"]
print("\nRows that are not OK:")
print(not_ok)

# Count each status, save the full report, and chart the status counts.
status_counts = df.groupby("status").size()
print("\nCount per status:")
print(status_counts)

df.to_csv("ai_dataset_report.csv", index=False)
print("\nSaved ai_dataset_report.csv")

status_counts.plot(kind="bar", title="AI Dataset Status Counts")
plt.tight_layout()
plt.savefig("ai_status_counts.png")
plt.close()
print("Saved ai_status_counts.png")
