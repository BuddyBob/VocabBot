# < run file here >
#if error occurs it will run again
#btw this is an updated version of https://github.com/snbk97/Vocabulary.com-AutoBot

import subprocess
import config
import time
import sqlite3
#connect to database
conn = sqlite3.connect('VocabBot.db')
#create cursor
c = conn.cursor()
times = []
#open times table
try:
    c.execute("""CREATE TABLE times(
                time float
            )""") 

except sqlite3.OperationalError as e:
    pass


def r():
    
    for i in range(config.TRIES):
        try:
            p = subprocess.call(['python3.8','./vocab_Demo.py'])
        except:
            pass


#get time of run
start = time.time()
r()
end = time.time()
end = round(end-start,3)

#Insert time into table
c.execute("INSERT INTO times VALUES (?)",(end,))
conn.commit()
#display all times
c.execute("select * from times")
empty = c.fetchall()
for tups in empty:
    times.append(tups[0])
count = 0
for i in reversed(times):
    count += 1
    print(f'Time {count}: {i}')