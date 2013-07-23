import logging.handlers as lh
import logging
import os
import glob
import sys

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

if len(sys.argv) < 2 or len(sys.argv) > 3:
    filename = raw_input('Log file name: ')
    try:
        numfiles = int(raw_input('Number of files: '))
    except Exception:
        print 'Invalid file count.'
        exit()
elif len(sys.argv) == 2:
    filename = sys.argv[1]
    try:
        numfiles = int(raw_input('Number of files: '))
    except Exception:
        print 'Invalid file count.'
        exit()
elif len(sys.argv) == 3:
    filename = sys.argv[1]
    numfiles = int(sys.argv[2])

if not os.path.exists(filename):
    print 'Invalid file path/name.'
    exit()
'''
try:
    f = open(filename)
except Exception:
    print 'Cannot open file. Be sure no other program is using it.'
    exit()
'''

locked = True

while locked:
    try:
        fh = lh.RotatingFileHandler(filename,
                            backupCount=numfiles)
        locked = False
    except Exception:
        print 'Cannot open file. Be sure no other program is using it.'
        locked = True

my_logger.addHandler(fh)
fh.doRollover()
# Essentially copy the log file to .out files
#for line in f:
    #my_logger.debug(line[:-1])

fh.close()
#f.close()
