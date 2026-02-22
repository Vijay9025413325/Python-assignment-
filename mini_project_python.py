import os

file_path = input("Enter log file path: ")

# Check if file exists 
if not os.path.exists(file_path):
    print("File not found.")
    exit()

file = open(file_path, "r")

error_count = 0
warning_count = 0
critical_count = 0
total_lines = 0

error_messages = {}

for line in file:
    total_lines += 1
    line = line.strip()

    if "ERROR" in line:
        error_count += 1
        if line in error_messages:
            error_messages[line] += 1
        else:
            error_messages[line] = 1

    elif "WARNING" in line:
        warning_count += 1

    elif "CRITICAL" in line:
        critical_count += 1

file.close()

# ================= VISUAL OUTPUT =================

print("\n" + "="*50)
print("            LOG ANALYSIS SUMMARY")
print("="*50)

print(f"{'Total Lines':<20}: {total_lines}")
print(f"{'Errors':<20}: {error_count}")
print(f"{'Warnings':<20}: {warning_count}")
print(f"{'Critical':<20}: {critical_count}")

# Percentage
if total_lines > 0:
    error_percentage = (error_count / total_lines) * 100
    print(f"{'Error %':<20}: {round(error_percentage,2)} %")

print("="*50)

# ================= VISUAL BAR GRAPH =================

def draw_bar(label, count):
    bar = "████" * count
    print(f"{label:<10} | {bar} ({count})")

print("\nLOG DISTRIBUTION")
print("-"*50)
draw_bar("ERROR", error_count)
draw_bar("WARNING", warning_count)
draw_bar("CRITICAL", critical_count)

# ================= MOST FREQUENT ERROR =================

most_common_error = ""
max_count = 0

for message in error_messages:
    if error_messages[message] > max_count:
        max_count = error_messages[message]
        most_common_error = message

if most_common_error != "":
    print("\nMost Frequent Error:")
    print("-"*50)
    print(most_common_error)
    print("Occurred:", max_count, "times")

# ================= ALERT SYSTEM =================

print("\nSYSTEM ALERTS")
print("-"*50)

if error_count >= 3:
    print("⚠ High number of errors detected!")

if critical_count >= 1:
    print("🚨 Critical issue detected!")

if error_count < 3 and critical_count == 0:
    print("System running within normal limits.")

# ================= SAVE REPORT =================

report_file = open("log_report.txt", "w")

report_file.write("===== LOG REPORT =====\n")
report_file.write(f"Total Lines: {total_lines}\n")
report_file.write(f"Errors: {error_count}\n")
report_file.write(f"Warnings: {warning_count}\n")
report_file.write(f"Critical: {critical_count}\n")

report_file.close()

print("\nReport saved as log_report.txt")
print("="*50)
