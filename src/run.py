# < run file here >
#if error occurs it will run again
#btw this is an updated version of https://github.com/snbk97/Vocabulary.com-AutoBot
import subprocess
import conrfig
for i in range(config.TRIES):
    #python version
    p = subprocess.call(['python3.8','vocab_Demo.py'])