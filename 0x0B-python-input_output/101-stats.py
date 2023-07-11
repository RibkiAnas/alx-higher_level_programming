#!/usr/bin/python3
"""
Script that reads stdin line by line and
computes metrics.
"""
import sys


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        total_size += int(data[-1])
        code_counts[int(data[-2])] += 1

        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(code_counts.keys()):
                if code_counts[code] > 0:
                    print(f"{code}: {code_counts[code]}")
except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {total_size}")
    for code in sorted(code_counts.keys()):
        if code_counts[code] > 0:
            print(f"{code}: {code_counts[code]}")
