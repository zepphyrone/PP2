import csv

csv_file_path = 'phonebook.csv'

new_data = [
    ["Aa", "707-549-4949"],
    ["Bb", "707-987-9876"]
]


with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(new_data)

print(f"data appended to {csv_file_path}")