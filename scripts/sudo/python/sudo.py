#!/usr/bin/python

'''
       Sudo for windows
'''

import os,sys,win32com.client

def getObject(name): 
    try: return win32com.client.Dispatch(name)
    except:
        print('ERROR: Failed to Dispatch Object : %s' % name)
        sys.exit()

uac = getObject('Shell.Application')
try:
    cmdx = "/a /k pushd " + os.getcwd() + " & " + ' '.join(sys.argv[1:])
    uac.ShellExecute("cmd.exe", cmdx, "", "runas", 1)
except:
    print('Unexpected error:', sys.exc_info()[0])
    raise
