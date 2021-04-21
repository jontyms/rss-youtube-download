import feedparser
import logging
import os
import time
from pathlib import Path
import pwd
import grp

logging.basicConfig(filename='vidoes.txt', level=logging.DEBUG, format='')
myfile = open("/root/youtube/rsss.txt", "r")
rssFeeds = []
myline = myfile.readline()
while myline:
    rssFeeds.append(myline)
    myline = myfile.readline()
myfile.close()  
print(rssFeeds)
for i in range(len(rssFeeds)):
 NewsFeed = feedparser.parse(rssFeeds[i])
 print(rssFeeds[i])
 for x in range(len(NewsFeed)):
  entry = NewsFeed.entries[x]
  logging.info(entry.link)
os.system("youtube-dl -i --dateafter now-1week -a vidoes.txt --download-archive ~/youtube/archive --add-metadata --embed-thumbnail --embed-subs --all-subs -o '~/youtube/%(uploader)s/%(title)s.%(ext)s' -f 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'")
print('done downloading videos')
os.remove("vidoes.txt") 
Path('vidoes.txt').touch()
uid = pwd.getpwnam("ubuntu").pw_uid
os.chown(~/youtube , uid)
time.sleep(3*60*60)