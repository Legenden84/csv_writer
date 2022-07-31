import csv

gender_is_female_and_like_rock_music = []

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
            gender_is_female_and_like_rock_music.append({
                'Gender': row['Gender'],
                'Favorite Music Genre': row['Favorite Music Genre']
            })

# Write new csv file
with open(
        'csv/gender.csv',
        'w',
        newline=''
) as gender_is_female_and_like_rock_music_csv:
    headers = ['Favorite Music Genre', 'Gender']
    csv_dict_writer = csv.DictWriter(gender_is_female_and_like_rock_music_csv, fieldnames=headers)
    csv_dict_writer.writeheader()

    for gender in gender_is_female_and_like_rock_music:
        csv_dict_writer.writerow(gender)
