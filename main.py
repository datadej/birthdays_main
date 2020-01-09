import argparse
import dbmanager
from birthdays_package import birthdays
from birthdays_package.pyscripts import data_reader

people_datafile = 'birthdays_package/data/people_infos.csv'
database_file = 'birthdays_package/data/database_file.db'

def parse_arguments():
    """Parse the arguments passed by the user

    :return: args
    :rtype: list
    """
    parser = argparse.ArgumentParser(
            description="Get name of someone you want to know the birthday of",
            prog="birthdays")
    # people infos can be added in the csv file in birthdays_package/data/
    parser.add_argument("name",
                        help='''The name of the person you want to know
                        the birthday of.''')
    parser.add_argument("-part", required=True,
                        choices = ['day','month','year','full'],
                        help="The part of the birthday you want to know")
    # one level of verbosity
    parser.add_argument("-v", help="Increase verbosity", action="store_true")
    parser.add_argument("--version", action="version", version="1.0")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # get people dictionary to retrieve the allowed names
    people = data_reader.parse_allowed_people(people_datafile)
    args = parse_arguments()
    birthday = birthdays.return_birthday(args.name, people, args.v)
    dbmanager.open_create(database_file)
    print(args)
    # if the person is not found in the dictionary
    if not birthday:
        print("Sorry, we don't have {}'s birthday".format(args.name))
    else:
        if args.part == 'day':
            print("{}'s birthday day is: {}".format(args.name, birthday[3:5]))
        elif args.part == 'month':
            print("{}'s birthday month is: {}".format(args.name,
                  birthday[0:2]))
        elif args.part == 'year':
            print("{}'s birthday year is: {}".format(args.name, birthday[-4:]))
        else:     
            print("{}'s birthday is: {}".format(args.name, birthday))

else:
    print("Please tell me the person you want to know the birthday of.")
    exit()
