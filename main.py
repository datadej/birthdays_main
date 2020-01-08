import argparse
from birthdays_package import birthdays
from birthdays_package.pyscripts import data_reader

people_datafile = 'birthdays_package/data/people_infos.csv'

def parse_arguments(people):
    """Parse the arguments passed by the user

    :param people: list of allowed names the user can get infos of
    :type people: list
    :return: arguments list
    :rtype: list
    """
    parser = argparse.ArgumentParser(
            description="Get name of someone you want to know the birthday of",
            prog="birthdays")
    parser.add_argument("name", choices = people,
                        help='''The name of the person you want to know
                        the birthday of.''')
    parser.add_argument("-v", help="Increase verbosity", action="store_true")
    parser.add_argument("--version", action="version", version="1.0")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    people = data_reader.parse_allowed_people(people_datafile)
    args = parse_arguments(list(people.keys()))
    name = args.name
    birthday = birthdays.return_birthday(name, people, args.v)
    # if the person is not found in the dictionary
    if not birthday:
        print("Sorry, we don't have {}'s birthday".format(name))
    else:
        print("{}' birthday is: {}".format(name, birthday))

else:
    print("Please tell me the person you want to know the birthday of.")
    exit()
