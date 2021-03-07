EMAIL = "email"
PASSWORD = "pwd"
#On mac it would look something like this - '/Users/Myname/Downloads/chromedriver'
#On windows it would look something like this - 'C:\Users\Myname\Downloads\chromedriver'
path_to_chromedriver = 'path'
#Note - keep quotes 'path'

#set this to a highnumber such as 100.
#errors will occur when a question has answers such as pictures or the question require you to type an answer
#   this will reset the program and start over. 
#       Setting it to 100 means if and error occurs it will start over. This process will happen 100 times. If this limit is exceeded
#           the program will quit
TRIES = 10