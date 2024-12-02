from pathlib import Path

INPUT_PATH = Path.cwd() / "inputfiles" / "day2.txt"

def import_input(file_path=INPUT_PATH):
    with open(file_path, "r") as f:
        return [line.rstrip('\n').split() for line in f]

def is_increasing(list):
    return all(i < j for i, j in zip(list, list[1:]))

def is_decreasing(list):
    return all(i > j for i, j in zip(list, list[1:]))

def diff_check(list):
    return all(abs(list[i]-list[i+1])<=3 for i in range(len(list)-1))

def is_safe(list):
    return diff_check(list) and (is_increasing(list) or is_decreasing(list))

def count_safe_reports(data):
    safe = 0
    for element in data:
        report = [int(number_string) for number_string in element]
        if(is_safe(report)):
            safe = safe + 1
        else:
            for i in range(len(report)):
                skipped_report = report[:i] + report[i+1:]
                if(is_safe(skipped_report)):
                    safe = safe + 1
                    break
    return safe

data = import_input()
safe_reports = count_safe_reports(data)
        
print(safe_reports)