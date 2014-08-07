#!/usr/bin/python
import ConfigParser
import os
import datetime

print 'backup.py 1.0'

# Read config from file.
config = ConfigParser.ConfigParser()
config.read("./backup.config")
username = config.get('login', 'user')
password = config.get('login', 'pass')
hostname = config.get('login', 'host')
database = config.get('db','database')

# human readable filenames for each weekday
days = {0:'0-monday', 1:'1-tuesday', 2:'2-wednesday', 3:'3-thursday', 4:'4-friday', 5:'5-saturday', 6:'6-sunday'}

# get date
today = datetime.datetime.today()

# get day of week, week, 
dayofweek = today.weekday()
week = today.isocalendar()[1]

# filename for daily and weekly backup files
dayfile = "./%s.sql" % (days[dayofweek])
weekfile = "./week-%s.sql" % (week)

# create a

# create a mysqldump for today
os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s > %s" % (username, password, hostname, database, dayfile))

# On Sunday make a copy for the weekly backup
if dayofweek == 6:
    os.popen("cp %s %s" % (dayfile, weekfile))
    os.popen("gzip -f %s" % (weekfile))
