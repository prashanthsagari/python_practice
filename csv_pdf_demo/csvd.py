import csv

data_lines = list(csv.reader(open('example.csv', encoding='utf-8')))
# ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']
full_name = []
emails = []
for line in data_lines[1:]:
    full_name.append(f'{line[1]} {line[2]}')
    emails.append(f'{line[3]}')
    


# Combine first name from names with emails
# combined = [(full_name[i], emails[i]) for i in range(len(full_name)-1)]
person_details = list(zip(full_name, emails))
# for person in person_details:
#     print(f'Name: {person[0]} Email: {person[1]}\n')
    
# writ into csv
file_to_output = open('person_details.csv', mode='w', newline='')
csv_data_writer = csv.writer(file_to_output, delimiter=',')
csv_data_writer.writerow(['Name','Email'])
csv_data_writer.writerows(person_details)
file_to_output.close()