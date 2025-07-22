success_count = 0
fail_count = 0

with open("C:/Users/HP/Documents/LoginAttemptsAnalyzer/log.txt", "r") as file:
    for line in file:
        if "SUCCESS" in line:
            success_count += 1
        elif "FAIL" in line or "ERROR" in line:
            fail_count += 1


print(f"Successful login attempts: {success_count}")
print(f"Failed login attempts: {fail_count}")


with open("C:/Users/HP/Documents/LoginAttemptsAnalyzer/report.txt", "w") as report:
    report.write(f"Successful login attempts: {success_count}\n")
    report.write(f"Failed login attempts: {fail_count}\n")
