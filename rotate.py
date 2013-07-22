import logging.handlers as lh
import logging
import os
import glob

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

filename = raw_input('Log file name: ')
try:
    filesize = int(raw_input('Size limit in MB: '))
except Exception:
    print 'Invalid file size.'
    exit()
    
try:
    numfiles = int(raw_input('Number of files: '))
except Exception:
    print 'Invalid file count.'
    exit()

if not os.path.exists(filename):
    print 'Invalid file path/name.'
    exit()
    
try:
    f = open(filename)
except Exception:
    print 'Cannot open file. Be sure no other program is using it.'
    exit()

try:
    fh = lh.RotatingFileHandler(filename+'.out',
                        maxBytes=filesize*1000000,backupCount=numfiles)
except Exception:
    print 'Cannot open file. Be sure no other program is using it.'
    exit()

my_logger.addHandler(fh)

# Essentially copy the log file to .out files
for line in f:
    my_logger.debug(line[:-1])

fh.close()
f.close()

# Rename the .out files to .log files
#os.remove(f)
os.rename(filename,filename+'.bak')

# See what files are created
logfiles = glob.glob('%s*' % (filename+'.out'))

for fname in logfiles:
    #print fname
    fsplit = fname.split('.')
    newname = fsplit[0]+'.'+fsplit[1]
    if len(fsplit) == 4:
        newname += '.'+fsplit[3]
    os.rename(fname,newname)
