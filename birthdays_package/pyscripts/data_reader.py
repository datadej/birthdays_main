import csv

def parse_allowed_people(datafile):
    with open(datafile) as people_data:
        people = {}
        csv_reader = csv.reader(people_data, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            name = row[0]
            birthday = row[1]
            people[name] = birthday
    return people