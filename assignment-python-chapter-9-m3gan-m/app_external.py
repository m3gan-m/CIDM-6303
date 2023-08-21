import subprocess

#run a command in the terminal
# ls -l means list files and folders with details
# ls -l uses lowercase l, not 1 (one)
subprocess.run(["ls","-l"])


#run some git commands.
#the arguments are entered as separate items in the list
subprocess.run(["git","--version"])
subprocess.run(["git","status"])
