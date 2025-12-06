"""
@date: 10/22/2025
@author: Ushnah Khan
@PID: ushnahk
@assignment: W9 CW Reading data off html
"""

import re
from pathlib import Path

# filenames
in_filename = 'student_list.html'
out_filename = 'student_list.txt'

# read the whole HTML file into a string
html_text = Path(in_filename).read_text(encoding='utf-8')

# Regex: match ONLY <td> rows (skips the header <th> row).
# Captures: first, last, year (digits)
row_pattern = re.compile(
    r"""
    <tr>\s*
        <td>\s*([^<]+)\s*</td>\s*   # first name
        <td>\s*([^<]+)\s*</td>\s*   # last name
        <td>\s*([0-9]+)\s*</td>\s*  # year
    </tr>
    """,
    flags=re.IGNORECASE | re.DOTALL | re.VERBOSE,
)

matches = row_pattern.findall(html_text)  # list of tuples: (first, last, year)

# Filter to FIRST-YEAR (year == '1'), normalize whitespace
records = []
for first, last, year in matches:
    first = first.strip()
    last = last.strip()
    year = year.strip()
    if year == '1':
        records.append((last, first, year))

# Sort by last, then first (case-insensitive)
records.sort(key=lambda t: (t[0].lower(), t[1].lower()))

# Write output: "Last, First" then year right-aligned (width 3 like a grade column)
lines = []
for last, first, year in records:
    lines.append(f"{last}, {first} {year.rjust(3)}")

Path(out_filename).write_text("\n".join(lines) + "\n", encoding='utf-8')

print(f"Wrote {len(records)} first-year students to {out_filename}")
