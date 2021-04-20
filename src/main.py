import feedparser
import logging
import os
import time

logging.basicConfig(filename='vidoes.txt', level=logging.DEBUG, format='')
myfile = open("~/youtube/rsss.txt", "r")
rssFeeds = []
myline = myfile.readline()
while myline:
    rssFeeds.append(myline)
    myline = myfile.readline()
myfile.close()  
print(rssFeeds)
for i in range(len(rssFeeds)):
 NewsFeed = feedparser.parse(rssFeeds[i])
 for x in range(len(NewsFeed)):
  entry = NewsFeed.entries[x]
  logging.info(entry.link)
os.system("youtube-dl -i --dateafter now-1week -a vidoes.txt --download-archive ~/.mydownloads --add-metadata --write-all-thumbnails --embed-thumbnail --write-info-json --embed-subs --all-subs -o '~/youtube/%(uploader)s/%(title)s.%(ext)s' -f 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'")
time.sleep(3*60)