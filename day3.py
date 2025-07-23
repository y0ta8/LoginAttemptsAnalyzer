from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

# Step 1: Read the log file
with open("C:/Users/HP/Documents/LoginAttemptsAnalyzer/log.txt", "r") as file:
    logs = file.readlines()

# Step 2: Classify login attempts
success_logins = [line for line in logs if "LOGIN SUCCESS" in line]
failed_logins = [line for line in logs if "LOGIN FAILURE" in line]

print(f"Successful login attempts: {len(success_logins)}")
print(f"Failed login attempts: {len(failed_logins)}")

# Step 3: Extract time (hour) from each attempt
time_format = "%Y-%m-%d %H:%M:%S"
login_hours = []

for line in logs:
    if "LOGIN SUCCESS" in line or "LOGIN FAILURE" in line:
        try:
            timestamp_str = line.split("LOGIN")[0].strip()  # e.g. '2025-07-15 12:01:05'
            time_obj = datetime.strptime(timestamp_str, time_format)
            login_hours.append(time_obj.hour)
        except ValueError:
            continue

# Step 4: Count login attempts per hour
hourly_counts = Counter(login_hours)

print("\nLogin attempts by hour:")
for hour, count in sorted(hourly_counts.items()):
    print(f"{hour:02d}:00 => {count} attempts")

# Step 5: Create bar chart
hours = list(range(24))
attempt_counts = [hourly_counts.get(h, 0) for h in hours]

plt.figure(figsize=(10, 5))
plt.bar(hours, attempt_counts, color="mediumseagreen")
plt.xlabel("Hour")
plt.ylabel("Number of Login Attempts")
plt.title("Login Attempts by Hour")
plt.xticks(hours)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("login_attempts_by_hour.png")
plt.show()

# Step 6: Generate text report
with open("report.txt", "w", encoding="utf-8") as report_file:
    report_file.write("Login Attempts by Hour:\n\n")
    for hour, count in sorted(hourly_counts.items()):
        report_file.write(f"{hour:02d}:00 => {count} attempts\n")

print("\nReport saved as 'report.txt'")
