from birthdays_package import birthdays
import sys

# if the user correctly provides a person name
if len(sys.argv) > 1:
    name = sys.argv[1]
    birthday = birthdays.return_birthday(name)
    # if the person is not found in the dictionary
    if not birthday:
        print("Sorry, we don't have {}'s birthday".format(name))
    else:
        print("{}' birthday is: {}".format(name, birthday))

else:
    print("Please tell me the person you want to know the birthday of.")
    exit()
