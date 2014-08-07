#!/usr/bin/python
import ConfigParser
import os
import datetime
import shutil

print 'backup.py 1.1'
print '#############'

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
dayfolder = "./%s" % (days[dayofweek])
weekfolder = "./week-%s" % (week)
dayfile = "./%s/%s.sql" % (days[dayofweek], database)
weekfile = "./week-%s.tar.gz" % (week)

# create folder if needed
if not os.path.exists(dayfolder):
    os.makedirs(dayfolder)

# create a mysqldump for today
print "creating sql dump      : %s" % (dayfile)
os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s > %s" % (username, password, hostname, database, dayfile))

# loop over folders and create archives
for folder in config._sections['folders']:
    if not folder == '__name__':
        archive = "%s/%s.tar.gz" % (dayfolder, folder)
        content = config.get('folders',folder)
        print "creating archive       : %s " % (archive)
        os.popen("tar -czf %s %s" % (archive, content))

# On Sunday make a copy for the weekly backup
if dayofweek == 6:
    print "creating weekly archive: %s" % (weekfile)
    shutil.copytree(dayfolder, weekfolder)
    os.popen("tar -czf %s %s" % (weekfile, weekfolder))

    print "deleting week folder   : %s" % (weekfolder)
    shutil.rmtree(weekfolder)

print '--==[ Done ]==--'