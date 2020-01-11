# Celebrities' Birthdays

In this repository you can find a file named ```main.py``` that gives you the birthday of a celebrity that it gets as a parameter.  
**Example**: run the main file using the following command: ```python main.py "Nicki Minaj" -part full -u test -p test``` and you will get the following result: 

```
$ python main.py "Nicki Minaj" -part full -u test -p test
Nicki Minaj's birthday is:  12/08/1982
```
> Note: user and password combination is required. You may want to create a new user before executing the example above. See the section **Managing users in the database.**



## Documentation

## Data Files
Celebrities and their birthdays are stored in a .csv file located in: ```birthday_package/data/```.  
**Some examples:**
Name | Birthday
------------ | -------------  
Rowan Atkinson|01/6/1955
Nicki Minaj|12/08/1982
Justine Ezarik|03/20/1984
Robin Williams|07/21/1981
Chris Brown|05/05/1989


## Positional and optional arguments
#### Positional arguments
- **name**: The name of the person you want to know the birthday of.
. 
#### Optional arguments
- **-h, --help:** show this help message and exit.
- **part {day, month, year, full}:** you can choose if you want to receive only the day/month/year of birth or the full birthday.
- **-u U [required]:** user's id
- **-p P [required]:** user's password 
- **-v:** Be more verbose.  
- **--version:** show program's version number and exit.

## Managing users in the database
In the main directory you can find a script called  ```dbmanager.py/``` that, when run, allows you to add or remove new users. Since **authentication is required**, you must create a user before executing the main script. The parameter **action** can be either *add* or *remove*, no other choices are allowed.

#### Add new user:
```
$ python main add -u USER_ID -p PASSWORD
```

```
$ python dbmanager.py add -u my_fantastic_id -p my_fantastic_password 
User my_fantastic_id added to the database
```

#### Removing a user
```
$ python main remove -u USER_ID
```

```
$ python dbmanager.py remove -u my_fantastic_id
Successfully removed user my_fantastic_id
```
## Tests
You can find tests here: ```birthday_package/tests_folder/``` .  Tests are provided for the following modules: ```test_data_reader.py``` and ```test_dbmanager.py```.  
You can run them **from the main directory** use:```python3 -m unittest -v -b birthdays_package/tests_folder/test_MODULENAME.py```:

```
python3 -m unittest -v -b birthdays_package/tests_folder/test_data_reader.py
test_empty_datafile (birthdays_package.tests_folder.test_data_reader.Test_data_reader) ... ok
test_file_is_not_csv (birthdays_package.tests_folder.test_data_reader.Test_data_reader) ... ok
test_no_datafile (birthdays_package.tests_folder.test_data_reader.Test_data_reader) ... ok
test_valid_file (birthdays_package.tests_folder.test_data_reader.Test_data_reader) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Authors:
- Gianluca Basso
- Giada Garbin
- Andrea Marino
- Dejvid Vangjelofski
