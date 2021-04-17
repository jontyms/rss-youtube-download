import feedparser
import logging
logging.basicConfig(filename='vidoes.txt', level=logging.DEBUG, format='')
myfile = open("rsss.txt", "r")
rssFeeds = []
myline = myfile.readline()
while myline:
    rssFeeds.append(myline)
    myline = myfile.readline()
myfile.close()  
print(rssFeeds)