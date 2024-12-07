# import csv

# # with open('euro_cup_matches.csv') as file:
# #     content = csv.DictReader(file)
# #     for row in content:
# #         print(row)

#     # headings = file.readline().strip()
#     # columns = headings.split(',')
#     # print(columns)
    
# total_goals = 0

# with open('euro_cup_matches.csv') as file:
#     content = csv.DictReader(file)
#     for row in content:
#         total_goals += int(row['Score A']) + int(row['Score B'])
        
# print(f'Total goals in tournament so far: {total_goals}')

# write csv
import csv

matches = [
    {
        'Team A': 'Portugal',
        'Team B': 'Spain',
        'Score A': 1,
        'Score B': 1,
        'Date': '2024-04-14' 
    },
    {
        'Team A': 'Germany',
        'Team B': 'France',
        'Score A': 1,
        'Score B': 3,
        'Date': '2024-04-21' 
    },
]

with open('new_matches.csv', 'w') as file:
    writer = csv.DictWriter(file, matches[0].keys())
    writer.writeheader()
    writer.writerows(matches)