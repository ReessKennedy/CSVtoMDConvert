import csv
import os

# Set the file location of the CSV
csv_file = "/Users/Reess/Desktop/RDConvert/RDExport.csv"

# Set the folder path for output
output_folder = "/Users/Reess/Desktop/RDConvert/MDFilesPY"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the CSV file
with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Group the data by calendar year and day
groups = {}
for row in data:
    created = row['created']
    year = created.split('-')[0]
    day = created.split('T')[0]
    key = f"{year}-{day}"
    groups.setdefault(key, []).append(row)

# Create markdown files for each year
for key, rows in groups.items():
    year = key[:4]
    markdown_file = os.path.join(output_folder, f"{year}bookmarks.md")

    with open(markdown_file, 'a') as file:
        # file.write(f"\n\n# {year}\n\n")

        # Group rows by day
        day_groups = {}
        for row in rows:
            day = row['created'].split('T')[0]
            day_groups.setdefault(day, []).append(row)

        # Write rows with date headers
        for day, day_rows in day_groups.items():
            file.write(f"\n## {day}\n\n")
            for row in day_rows:
                url = row['url'].strip()
                title = row['title'].strip()
                excerpt = row['excerpt'].strip()
                note = row['note'].strip()
                highlights = row['highlights'].strip()

                # Replace "```" elements in values
                url = url.replace("```", "&#96;&#96;&#96;")
                title = title.replace("```", "&#96;&#96;&#96;")
                excerpt = excerpt.replace("```", "&#96;&#96;&#96;")
                note = note.replace("```", "&#96;&#96;&#96;")
                highlights = highlights.replace("```", "&#96;&#96;&#96;")

                # Check if any field in the row contains data
                if any(field for field in [url, title, excerpt, note, highlights]):
                    file.write(f"{url}\n")
                    file.write("```\n")
                    if title:
                        file.write(f"{title}\n")
                    if excerpt:
                        file.write(f"{excerpt}\n")
                    if note:
                        file.write(f"{note}\n")
                    if highlights:
                        file.write(f"{highlights}\n")
                    file.write("```\n\n")

print("Markdown files created successfully.")
