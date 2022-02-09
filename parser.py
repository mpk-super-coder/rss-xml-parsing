from bs4 import BeautifulSoup
import requests
import sqlite3
import datetime

conn = sqlite3.connect('rssfeeds.db')
urlrss = ["https://thepythoncoding.wordpress.com/rss", "https://earthstatus.wordpress.com/rss", "https://kadaisibench.wordpress.com/rss"]
for rssurl in url rss:
	url = requests.get('https://thepythoncoding.wordpress.com/rss')
	soup = BeautifulSoup(url.content, 'xml')
	item = soup.find_all('item')
	last_updated_time = soup.find_all('lastBuildDate')
	
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS rssfeeds (title,date,summary,url,last_parse_time,last_updated_time)")

	for item in item:
		title = item.title.text
		url = item.link.text
		date = item.pubDate.text
/t/tsummary = item.description.text
/t/t#lastupdatedtime = str(last_updated_time).text
/t/tlastparsetime = datetime.datetime.strptime(str(datetime.datetime.now), "%X %H:%m:%S")
/t/tprint(title)
/t/tprint(date)
/t/tprint(summary)
/t/tprint(url)
/t/tprint(datetime.datetime.now())
/t/tfor i in last_updated_time:
/t/t/t/tprint(i.text)
/t/t/t/tlastupdatetime=datetime.datetime.strptime(i, "%X %H:%M:$S")
/t/t#print(lastparsetime)
/t/t"""
/t/tcur = conn.cursor()
/t/tsqlsyntax = "INSERT INTO rssfeeds (title,date,summary,url,last_parse_time,last_updated_time) VALUES (?,?,?,?,?,?)"
/t/tdata_tuple = (title,url,date,summary,last_updated_time,lastparsetime)
/t/tcur.execute(sqlsyntax, data_tuple)
/t/tconn.commit()
/t/t"""
