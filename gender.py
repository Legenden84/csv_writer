import csv

temp_csv = []

# Read csv
with open('datasets/gender.csv', 'r') as dataset_csv:
    csv_dict_reader = csv.DictReader(dataset_csv)

    for row in csv_dict_reader:
        # Gender must be female.
        # Female favorite music must be Rock.
        gender = row['Gender']
        music = row['Favorite Music Genre']
        if gender == 'F' and music == 'Rock':
            # Parse csv
            temp_csv.append({
                'Gender': row['Gender'],
                'Favorite Music Genre': row['Favorite Music Genre']
            })

# Write new csv file
with open(
        'csv/gender.csv',
        'w',
        newline=''
) as csv_write:
    headers = ['Favorite Music Genre', 'Gender']
    csv_dict_writer = csv.DictWriter(csv_write, fieldnames=headers)
    csv_dict_writer.writeheader()

    for gender in temp_csv:
        csv_dict_writer.writerow(gender)
