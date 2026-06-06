##import warnings
##warnings.simplefilter("ignore")
##from bs4 import BeautifulSoup # this module helps in web scrapping.
##import requests  # this module helps us to download a web page
#html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
#soup = BeautifulSoup(html, "html.parser")
##print(soup.prettify())
##print(soup)
#tag_object = soup.h3
#tag_child = tag_object.parent
#sibling_1 = tag_object.next_sibling
#print("tag object:",tag_object)
#print("tag object type:",type(tag_object))
#print("tag object type:",(tag_child['id']))
#print("tag object type:",(sibling_1))/*

#_____________________________
#table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"
#table_bs = BeautifulSoup(table, "html.parser")
#table_rows=table_bs.find_all('tr')
#first_row =table_rows[0]
#print(type(first_row))

#for i,row in enumerate(table_rows):
#    print("row",i)
 #   cells=row.find_all('td')
  #  for j,cell in enumerate(cells):
   #     print('colunm',j,"cell",cell)

#list_input=table_bs .find_all(name=["tr", "td"])
#print (list_input)

##url = "https://web.archive.org/web/20230224123642/https://www.ibm.com/us-en/"
##data  = requests.get(url).text 
##soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
##for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
  ##  print(link.get('href'))

import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text
##print(data)
soup = BeautifulSoup(data, 'html.parser')
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)    
print (netflix_data.head())




#read_html_pandas_data = pd.read_html(url)
#from io import StringIO

#read_html_pandas_data = pd.read_html(StringIO(str(soup)))
#netflix_dataframe = read_html_pandas_data[0]

#print (netflix_dataframe.head())