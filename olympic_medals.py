import csv

temp_csv = []

# Read csv
with open('datasets/olympic_medals.csv', 'r') as dataset_csv:
    csv_dict_reader = csv.DictReader(dataset_csv)
    # out commented method is used to extract every header.
    # headers = next(csv_dict_reader)

    for row in csv_dict_reader:
        # Summer or winter medals more than 100.

        summer_gold = int(row['summer_gold'])
        summer_silver = int(row['summer_silver'])
        summer_bronze = int(row['summer_bronze'])
        winter_gold = int(row['winter_gold'])
        winter_silver = int(row['winter_silver'])
        winter_bronze = int(row['winter_bronze'])

        if (summer_gold + summer_silver + summer_gold) >= 100 or (winter_gold + winter_silver + winter_bronze) >= 100:
            temp_csv.append({
                'countries ': row['countries '],
                'summer_gold': row['summer_gold'],
                'summer_silver': row['summer_silver'],
                'summer_bronze': row['summer_bronze'],
                'winter_gold': row['winter_gold'],
                'winter_silver': row['winter_silver'],
                'winter_bronze': row['winter_bronze']
            })

# Write new csv file
with open(
    'csv/olympic_medals.csv',
    'w',
    newline=''
) as csv_write:
    headers = ['countries ', 'summer_gold', 'summer_silver', 'summer_bronze', 'winter_gold', 'winter_silver', 'winter_bronze']
    csv_dict_writer = csv.DictWriter(csv_write, fieldnames=headers)
    csv_dict_writer.writeheader()

    for medals in temp_csv:
        csv_dict_writer.writerow(medals)
