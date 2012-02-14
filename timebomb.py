#!/usr/bin/python
# A Pythonic Time Bomb
# Kills Processes Living Longer than the specified time.
# Don't Forget to add it to your crontab!
# http://github.com/eaydin

import subprocess, sys
if len(sys.argv) != 3 :
    print "Usage : timebomb.py <process-name> <time-in-minutes>"
    print "Takes only and exactly 2 arguments."
    raise SystemExit
    
try : int(sys.argv[2])
except :
    print "%s is not an integer." % sys.argv[2]
    raise SystemExit
    
try :
    a=subprocess.Popen(["pgrep",sys.argv[1]],stdout=subprocess.PIPE).communicate()[0]
    if a == '' :
        raise SystemExit
    else :
        procc = subprocess.Popen(["ps -o pid,bsdtime -p $(pgrep %s)"%(sys.argv)[1]],shell=True,stdout=subprocess.PIPE).communicate()[0]
        procc=procc.strip()
except : raise SystemExit 
for lines in procc.split('\n') :
    if lines != '' :
        l=lines.split()
        if l[0] == 'PID' : pass
        else :
            if int(l[1].split(':')[0]) >= int(sys.argv[2]) :
                try : killer = subprocess.Popen(["kill","-9",l[0]],stdout=subprocess.PIPE).communicate()[0]
                except : pass
            else : pass
