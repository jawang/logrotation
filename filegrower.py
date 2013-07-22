from time import *
import os

for i in range(10000):
    fh = open('asdf.log','a')
    s = ''
    for j in range(1000):
        s += str(i)
    sleep(0.5)
    fh.write(s+'\n')
    fh.close()
