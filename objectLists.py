import subprocess as sp

listObjects = sp.Popen(['ls','res/objects'],stdout=sp.PIPE,stderr=sp.STDOUT)
stdout,stderr = listObjects.communicate()
LIST = stdout.decode('UTF-8','strict').split('.mo\n')[:-1]

AOL=LIST
AOL_t=AOL
