birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}


def print_birthdays():
    """print names of people in birthdays dictionary

    The birthdays dictionary contains names as keys and birthdays as values.
    When the function is invoked, it returns the names of the people in the
    dictionary built in the program

    :return: None
    :rtype: Boolean
    """
    print('''Welcome to the birthday dictionary.
          We know the birthdays of these people:''')
    for name in birthdays:
        print(name)


def return_birthday(name, verbosity):
    """print the birthday of a person

    The birthdays dictionary contains names as keys and birthdays as values.
    When this function is invoked, it returns the birthday of the person
    received as a parameter if the value exists in the dictionary, False
    otherwise.

    :param name: the name of the person
    :type name: string
    :param verbosity: The verbosity wanted by the user
    :type verbosity: Boolean
    :return: The birthday of the person passed as parameter or False
    :rtype: String or Boolean
    """
    # if the name is present in the dictionary
    if verbosity:
        print("Started looking for {}'s birthday".format(name))
    if name in birthdays:
        return birthdays[name]
    else:
        return False
    
