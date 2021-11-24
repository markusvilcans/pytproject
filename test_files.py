#Program to test if all necessary files are present
import os.path
os.chdir(os.path.dirname(__file__))

print('Checking if config file exists in working directory.')
assert os.path.isfile('config.ini') == True
print('File exists.\n')

print('Checking if log file exists in working directory.')
assert os.path.isfile('log.log') == True
print('File exists.\n')

print('Checking if migrate_db.py file exists in working directory.')
assert os.path.isfile('migrate_db.py') == True
print('File exists.\n')

print('Checking if naked.py file exists in working directory.')
assert os.path.isfile('naked.py') == True
print('File exists.\n')

print('Checking if readme.md file exists in working directory.')
assert os.path.isfile('readme.md') == True
print('File exists.\n')

print('Checking if words_database.txt file exists in working directory.')
assert os.path.isfile('words_database.txt') == True
print('File exists.\n')

print('Checking if worker_db.py file exists in working directory.')
assert os.path.isfile('worker_db.py') == True
print('File exists.\n')