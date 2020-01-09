import csv


def parse_allowed_people(datafile):
    """Read people names and birthdays from csv file

    :param datafile: the path to the csv file
    :type datafile: string
    :return: The dictionary containing names and birthdays
    :rtype: Dictionary Object
    """
    try:
        with open(datafile) as people_data:
            people = {}
            csv_reader = csv.reader(people_data)
            next(csv_reader)
            for row in csv_reader:
                name = row[0]
                birthday = row[1]
                people[name] = birthday
        return people
    except:
        return False
