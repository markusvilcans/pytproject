#Program to test if config info is correct and connection to MySQL DB is successful
import os.path
import mysql.connector
from configparser import ConfigParser

os.chdir(os.path.dirname(__file__))

print('Checking if config file exists in working directory.')
assert os.path.isfile('config.ini') == True
print('File exists.\n')

config = ConfigParser()
config.read('config.ini')

print('Checking if config file has the necessary information to connect to DB.')
assert config.has_option('mysql_config','mysql_host') == True
assert config.has_option('mysql_config','mysql_db') == True
assert config.has_option('mysql_config','mysql_user') == True
assert config.has_option('mysql_config','mysql_pass') == True

print('Checking the connection to DB.')
mysql_config_mysql_host = config.get('mysql_config','mysql_host')
mysql_config_mysql_db = config.get('mysql_config','mysql_db')
mysql_config_mysql_user = config.get('mysql_config','mysql_user')
mysql_config_mysql_pass = config.get('mysql_config','mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print('Connection successful.')

