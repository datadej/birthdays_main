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
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    """print the birthday of a person
    
    The birthdays dictionary contains names as keys and birthdays as values.
    When this function is invoked, it returns the birthday of the person
    received as a parameter.
    
    :param name: the name of the person
    :type name: string
    :return: None
    :rtype: None
    """
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))