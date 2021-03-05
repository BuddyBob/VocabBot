# Vocabulary.com bot

This is a bot which can finish your vocabulary.com homework for you!

## Prerequisets
  <pre>
    * Chrome Driver [<a href="https://sites.google.com/a/chromium.org/chromedriver/">Link</a>] placed in the correct folder
    * Selenium python module - $ pip3 install selenium
    * Unicode python module - $ pip3 install unicode 
    * BeautifulSoup4 python module - $ pip3 install BeautifulSoup4
    * urllib3.request - $ pip3 install urllib3
  </pre>
## How to run
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Edit config file**
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Located in <code>src</code> is a config file
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Change the nessaccary variables in there - save
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Run main file**
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Located in <code>src</code> is a <code>run.py</code> file - cd to the file
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the file - python3 run.py
  
  
## Errors
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Which questions are not supported**
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Fill in the blank
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Select the picture
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Spell it

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Reasons chrome browswer might quit**
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Question was not supported
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Your vocab list could not be loaded
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Requests to open page canceled
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - *Selenium*: Button or Text not loaded in time
  
## Remember to
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; || Keep the google chrome browswer open at all times ||
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; || Do not share this code with others before removing your information from the config file ||
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; || If you would like, add links to lines 17-20 ; #lines that you dont need, remove # one lines you need || 
  
```python 
    #url = "https://www.vocabulary.com/lists/23380/practice"
    #url = "https://www.vocabulary.com/lists/7701690/practice"
    #url = "https://www.vocabulary.com/lists/52473/practice"
    url = "https://www.vocabulary.com/lists/194479/practice"
```

  
  
  

  
  
  
  