import urllib2 
import re
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='',db='test')
x = conn.cursor()
request = urllib2.Request("https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1") 
response = urllib2.urlopen(request) 
quora_page = response.read() #Response from the page
allips = re.sub(re.compile("#.*?\n"),"",quora_page)#Regular expression to filter any comments in the page response.
for line in allips.split('\n'): #Counting number of ip on the page and getting ip address from each line
    x.execute("INSERT INTO ips(ip) VALUES (%s)", line) #Inserting values in to the database
    conn.commit()
x.execute("DELETE from ips where ip=''") #deleting any row if emply line is inserted in.
conn.commit()
x.close()
conn.close()